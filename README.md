# Makhraj Auto World

MVP monorepo for Makhraj Auto World's business website.

## Architecture

- `frontend/` will contain the Next.js App Router application (React, TypeScript, Tailwind CSS).
- `backend/` contains the FastAPI REST API and will use SQLAlchemy with PostgreSQL.
- `docs/` contains the supplied product and information-architecture documents.

The frontend will consume a versioned REST API. Runtime configuration is supplied through environment variables; no real business data or credentials are stored in this repository.

## Current milestone

The first milestone establishes a safe project foundation and a minimal API health endpoint. Database entities, authentication, and UI are deferred to later milestones.

## Run the backend locally

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Set a real PostgreSQL connection and a long random `SECRET_KEY` in `.env`. The health endpoint is `http://127.0.0.1:8000/api/v1/health`.

## Frontend

The Next.js application will be initialized in the next milestone. Its API base URL is documented in `frontend/.env.example`.
