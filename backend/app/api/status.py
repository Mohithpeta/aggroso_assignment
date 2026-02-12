from fastapi import APIRouter
from app.core.config import settings
import os

router = APIRouter(prefix="/status", tags=["status"])


@router.get("")
def status():
    storage_ok = os.path.exists("app/storage")

    return {
        "backend": "ok",
        "storage": "ok" if storage_ok else "missing",
        "llm": "configured" if settings.openai_api_key else "missing_api_key",
    }