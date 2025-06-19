# TODO for Stock Dashboard UI

## 1. UI Features

- [ ] Add chart visualizations using `recharts` or `chart.js`
- [ ] Add filter and search controls for stock symbols
- [ ] Add pagination or infinite scroll for long data lists
- [ ] Support dark mode toggle
- [ ] Responsive layout for mobile and tablet devices

## 2. API Integration

- [ ] Connect to backend REST endpoints for live data
- [ ] Add error handling and loading states for API calls
- [ ] Add WebSocket or SSE support for live updates

## 3. Testing

- [ ] Add full unit test coverage for all components
- [ ] Snapshot tests for reusable components
- [ ] E2E testing setup with Playwright or Cypress (optional)

## 4. Security & Compliance

- [ ] Enable REUSE license headers
- [ ] Enable SBOM and provenance (SLSA/CycloneDX)
- [ ] Run semgrep static analysis for frontend security
- [ ] Run `secretlint` to scan for secrets in config files

## 5. Build & Deployment

- [ ] Harden Dockerfile for production
- [ ] Finalize Helm values for environment-specific config
- [ ] Add healthcheck endpoint and probe readiness

## 6. Documentation

- [ ] Setup Docusaurus for frontend developer documentation
- [ ] Add storybook support (optional)
- [ ] Document supported API contracts and expected inputs/outputs
