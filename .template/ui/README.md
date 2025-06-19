# Stock Dashboard UI

This repository contains the frontend for the stock analytics dashboard, built using **Next.js**, **React**, **Tailwind CSS**, and **TypeScript**. It displays stock data, sentiment scores, technical indicators, and custom visualizations sourced from backend microservices.

## ✅ Features

- Modular React-based UI with dynamic routing
- Type-safe frontend using TypeScript
- Styled with Tailwind CSS for rapid design
- Integrated with RabbitMQ, InfluxDB, and PostgreSQL via backend APIs
- Authentication-ready structure (optional future enhancement)
- Dockerized for local and production deployment
- Helm chart for Kubernetes deployments with ArgoCD support

## 🗂️ Project Structure

```
.
├── public/                 # Static assets
├── src/
│   ├── components/         # Reusable UI components
│   ├── pages/              # Next.js routes
│   ├── styles/             # Global CSS (Tailwind)
│   ├── utils/              # Frontend utility functions
│   └── types/              # TypeScript interfaces and enums
├── .github/                # GitHub Actions and workflows
├── Dockerfile              # Production Docker build
├── docker-compose.yml      # Local dev environment
├── Makefile                # Standardized dev tasks
├── helm/                   # Helm chart for K8s deployment
└── README.md
```

## 🛠️ Local Development

```bash
make install
make dev
```

Or directly:

```bash
npm install
npm run dev
```

## 🧪 Testing

```bash
make test
# or
npm run test
```

Unit testing is handled by [Vitest](https://vitest.dev/) and coverage by [c8](https://github.com/bcoe/c8).

## 🚀 Deployment

### Docker

```bash
docker build -t stock-dashboard-ui .
docker run -p 3000:3000 stock-dashboard-ui
```

### Kubernetes

```bash
make helm-install
```

## 🧰 Tooling

- [Next.js](https://nextjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [TypeScript](https://www.typescriptlang.org/)
- [Vitest](https://vitest.dev/)
- [ESLint + Prettier](https://eslint.org/)
- [Commitizen](https://github.com/commitizen/cz-cli)

## 📝 License

Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
