from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.openai_api_key)

def answer_question(question: str, contexts: list[dict]) -> str:
    context_text = "\n\n".join(
        f"[{c['document']}]\n{c['chunk']}" for c in contexts
    )

    prompt = f"""
You are answering questions using ONLY the provided context.
If the answer is not in the context, say you don't know.

Context:
{context_text}

Question:
{question}

Answer:
"""

    try:
        response = client.chat.completions.create(
            model=settings.chat_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return response.choices[0].message.content.strip()

    except Exception:
        # Fallback when LLM is unavailable
        return (
            "The language model is currently unavailable. "
            "Here are the most relevant excerpts from the uploaded documents."
        )