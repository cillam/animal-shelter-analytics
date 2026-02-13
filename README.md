# Shelter Analytics Platform

A full-stack application for shelter animal analytics, outcome prediction, and adoption bio generation.

## Features

- **Dashboard**: Shelter-wide statistics, at-risk animals, resource allocation insights
- **Outcome Prediction**: Naive Bayes model predicting positive/negative outcomes
- **Length of Stay Prediction**: Regression model for resource planning
- **Bio Generator**: AI-powered adoption profile generator using Claude Vision

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React + Vite |
| Frontend Hosting | Azure Static Web Apps |
| Backend | Python + FastAPI |
| Backend Compute | Azure Container Apps |
| Data Platform | Azure Databricks |
| Database | Azure SQL |
| Dashboards | Power BI Embedded |
| IaC | Terraform |
| CI/CD | GitHub Actions |

## Project Structure

```
shelter-analytics/
├── .github/workflows/     # CI/CD pipelines
├── frontend/              # React application
├── backend/               # FastAPI application
├── terraform/             # Infrastructure as code
├── databricks/            # Databricks notebooks
└── powerbi/               # Power BI dashboard files
```

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 20+
- Poetry
- Azure CLI
- Terraform

### Backend Setup

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Running Tests

```bash
# Backend
cd backend
poetry run pytest

# Frontend
cd frontend
npm run test
```

## Deployment

- **Staging**: Merges to `dev` branch deploy to staging environment
- **Production**: Merges to `main` branch deploy to production environment

## License

MIT
