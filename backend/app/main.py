from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.core.config import get_settings

settings = get_settings()
app = FastAPI(title="Makhraj Auto World API", version="0.1.0", redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)
app.include_router(health_router, prefix="/api/v1")
