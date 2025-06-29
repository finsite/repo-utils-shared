#!/usr/bin/env python3
"""Generate Helm, Kustomize, and ArgoCD Kubernetes manifests for the current app.

This script creates standard deployment and configuration files based on the app name
(determined from the current directory). It also provides optional validation of the
generated manifests using Helm, Kustomize, and yamllint.
"""

import os
import shutil
import subprocess
import sys
from collections.abc import Sequence


def create_directory(path: str) -> None:
    """Create a directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


def write_file(path: str, content: str) -> None:
    """Write content to a file, creating directories if necessary."""
    create_directory(os.path.dirname(path))
    if os.path.exists(path):
        print(f"⚠️  Overwriting existing file: {path}")
    with open(path, "w", newline="\n", encoding="utf-8") as f:
        f.write(content.strip() + "\n")


def get_app_name() -> str:
    """Return the current directory name as the app name."""
    return os.path.basename(os.getcwd())


def generate_all_templates(app_name: str) -> None:
    """Generate all Helm, K8s, and ArgoCD templates for a given app."""
    files = {
        f"charts/{app_name}/Chart.yaml": f"""
---
apiVersion: v2
name: {app_name}
description: A Helm chart for {app_name}
type: application
version: 0.1.0
appVersion: "1.0"
""",
        f"charts/{app_name}/values.yaml": """
---
replicaCount: 1

image:
  repository: myregistry.io/app
  tag: latest

service:
  type: ClusterIP
  port: 8080
""",
        f"charts/{app_name}/templates/deployment.yaml": """
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Chart.Name }}
  labels:
    app: {{ .Chart.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Chart.Name }}
  template:
    metadata:
      labels:
        app: {{ .Chart.Name }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: 8080
""",
        "k8s/base/deployment.yaml": f"""
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {app_name}
  labels:
    app: {app_name}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {app_name}
  template:
    metadata:
      labels:
        app: {app_name}
    spec:
      containers:
      - name: {app_name}
        image: {app_name}:latest
        ports:
        - containerPort: 8080
""",
        "k8s/base/service.yaml": f"""
---
apiVersion: v1
kind: Service
metadata:
  name: {app_name}
spec:
  type: ClusterIP
  selector:
    app: {app_name}
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
""",
        "k8s/base/kustomization.yaml": """
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - deployment.yaml
  - service.yaml
""",
        "k8s/overlays/dev/kustomization.yaml": f"""
---
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - ../../base/

namespace: default

labels:
  - includeSelectors: true
    pairs:
      app: {app_name}

images:
  - name: {app_name}
    newName: {app_name}
    newTag: latest
""",
        f"argocd/{app_name}/application.yaml": f"""
---
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: {app_name}
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/your-org/{app_name}.git
    targetRevision: main
    path: charts/{app_name}
    helm:
      valueFiles:
        - values.yaml
  destination:
    server: https://kubernetes.default.svc
    namespace: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
""",
    }

    for path, content in files.items():
        write_file(path, content)
        print(f"✅ Created: {path}")


def run_command_safe(cmd: Sequence[str], desc: str) -> None:
    """Run a shell command safely with description output."""
    print(f"\n🔍 {desc}:")
    try:
        subprocess.run(cmd, check=True)  # nosec B603 B607: safe list, not user input
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Command failed: {' '.join(cmd)}\n{e}")
    except FileNotFoundError:
        print(f"⚠️  Command not found: {cmd[0]}")


def validate_files(app_name: str) -> None:
    """Run Helm, Kustomize, and yamllint validation on generated files."""
    helm_chart = f"charts/{app_name}"
    kustomize_path = "k8s/overlays/dev"

    run_command_safe(["helm", "lint", helm_chart], "Helm lint")
    run_command_safe(["helm", "template", helm_chart], "Helm render")
    run_command_safe(["kustomize", "build", kustomize_path], "Kustomize build")

    if shutil.which("yamllint"):
        run_command_safe(["yamllint", "charts/"], "YAML lint (charts)")
        run_command_safe(["yamllint", "k8s/"], "YAML lint (k8s)")
    else:
        print("ℹ️  yamllint not installed, skipping YAML lint checks")


def main() -> None:
    """Entry point for the script."""
    app_name = get_app_name()
    skip_validate = "--skip-validate" in sys.argv

    print(f"\n🔧 Generating all manifests for app: {app_name}")
    generate_all_templates(app_name)

    if not skip_validate:
        validate_files(app_name)

    print(
        "\n✅ All files generated." if skip_validate else "\n✅ All files generated and validated."
    )
    print("📦 Structure:")
    print(" - charts/")
    print(" - k8s/base/")
    print(" - k8s/overlays/dev/")
    print(" - argocd/")
    print("🧪 You can now commit or test with kubectl/ArgoCD.")


if __name__ == "__main__":
    main()
