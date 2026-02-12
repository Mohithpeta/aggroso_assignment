from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.embeddings import embed_texts
from app.services.vectorstore import VectorStore
from app.services.qa_service import answer_question

router = APIRouter(prefix="/ask", tags=["qa"])

vector_store = VectorStore(dim=1536)


class QuestionRequest(BaseModel):
    question: str


@router.post("")
def ask_question(payload: QuestionRequest):
    if not payload.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    try:
        # Try embedding (may fail if OpenAI quota is 0)
        query_embedding = embed_texts([payload.question])[0]
        results = vector_store.search(query_embedding, k=3)

    except Exception:
        # Embeddings unavailable or FAISS empty
        return {
            "answer": "The language model is currently unavailable.",
            "sources": []
        }

    if not results:
        return {
            "answer": "I don't know based on the uploaded documents.",
            "sources": []
        }

    try:
        answer = answer_question(payload.question, results)
    except Exception:
        answer = (
            "The language model is currently unavailable. "
            "Here are the most relevant document excerpts."
        )

    return {
        "answer": answer,
        "sources": results
    }