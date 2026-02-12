from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import json

from app.services.loader import chunk_text
from app.services.embeddings import embed_texts
from app.services.vectorstore import VectorStore

router = APIRouter(prefix="/upload", tags=["documents"])

DOC_DIR = "app/storage/documents"
CHUNK_DIR = "app/storage/chunks"

os.makedirs(DOC_DIR, exist_ok=True)
os.makedirs(CHUNK_DIR, exist_ok=True)

# Embedding dimension for text-embedding-3-small
vector_store = VectorStore(dim=1536)


@router.post("")
async def upload_document(file: UploadFile = File(...)):
    # ---- Validation ----
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are allowed")

    # ---- Read file ONCE ----
    raw_bytes = await file.read()

    if not raw_bytes or not raw_bytes.strip():
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    try:
        content = raw_bytes.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="File must be UTF-8 encoded text"
        )

    if not content.strip():
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    # ---- Save document ----
    file_path = os.path.join(DOC_DIR, file.filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    # ---- Chunk document ----
    chunks = chunk_text(content)
    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="Failed to process document content"
        )

    # ---- Persist chunks ----
    chunk_path = os.path.join(
        CHUNK_DIR, file.filename.replace(".txt", ".json")
    )
    with open(chunk_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2)

    # ---- Try embedding + indexing ----
    indexed = True
    try:
        embeddings = embed_texts(chunks)
        metadatas = [
            {"document": file.filename, "chunk": chunk}
            for chunk in chunks
        ]
        vector_store.add(embeddings, metadatas)
    except Exception:
        indexed = False

    return {
        "filename": file.filename,
        "chunks_created": len(chunks),
        "indexed": indexed,
        "message": (
            "Document uploaded and indexed successfully"
            if indexed
            else "Document uploaded, but indexing is pending (LLM unavailable)"
        ),
    }