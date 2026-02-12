from fastapi import APIRouter
import os

router = APIRouter(prefix="/documents", tags=["documents"])

DOC_DIR = "app/storage/documents"


@router.get("")
def list_documents():
    files = os.listdir(DOC_DIR) if os.path.exists(DOC_DIR) else []
    return {"documents": files}