# Makhraj Auto World

MVP monorepo for Makhraj Auto World's business website.

## Architecture

- `frontend/` will contain the Next.js App Router application (React, TypeScript, Tailwind CSS).
- `backend/` contains the FastAPI REST API and will use SQLAlchemy with PostgreSQL.
- `docs/` contains the supplied product and information-architecture documents.

The frontend will consume a versioned REST API. Runtime configuration is supplied through environment variables; no real business data or credentials are stored in this repository.

## Current progress

The project includes the initial FastAPI foundation, SQLAlchemy database session management, the Admin ORM model, Argon2id password hashing, and an Alembic migration for the `admins` table. Public API resources, login, and dashboard workflows are implemented in later milestones.

## Run the backend locally

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Set a real PostgreSQL connection and a long random `SECRET_KEY` in `.env`.

## Initialize the development database

1. Create a local PostgreSQL database and a dedicated application user with only the permissions needed for this application.
2. Set `DATABASE_URL` in `backend/.env`, for example:

   ```text
   DATABASE_URL=postgresql+psycopg://<application-user>:<password>@localhost:5432/makhraj_auto_world
   ```

3. Apply the reviewed migrations before starting the API:

   ```powershell
   cd backend
   alembic upgrade head
   ```

4. Start the API with `uvicorn app.main:app --reload`.

The health endpoint is `http://127.0.0.1:8000/api/v1/health`.

## Frontend

The Next.js App Router foundation is in `frontend/`. Its API base URL is documented in `frontend/.env.example`.

```powershell
cd frontend
npm.cmd install
npm.cmd run dev
```
