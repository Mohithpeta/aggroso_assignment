# Private Knowledge Q&A (Mini RAG Workspace)

A simple web application that allows users to upload text documents, index them, and ask questions grounded only in the uploaded content. The system is designed to be robust, explainable, and easy to run locally or in Docker.

---

## Features

- Upload `.txt` documents
- Persist uploaded documents and processed chunks
- View list of indexed documents (persists across refresh and restart)
- Ask questions against uploaded documents
- See which document chunks were used as sources
- Graceful handling when external LLM or embedding services are unavailable
- Single-page UI served directly by the backend
- Dockerized setup (runs with one command)

---

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** Vanilla HTML, CSS, JavaScript (served as static files)
- **Vector Store:** FAISS (local)
- **Embeddings / LLM:** OpenAI (with graceful fallback when unavailable)
- **Containerization:** Docker + Docker Compose

---

## How to Run (Docker – Recommended)

### Prerequisites
- Docker
- Docker Compose

### Steps

1. Clone the repository
   ```bash
   git clone 
   cd agrosso_assignment

2. Create environment file

cp backend/.env.example backend/.env

Note: An OpenAI API key is optional. The app runs without it.

3. Build and start the app

docker compose up --build

4. Open in browser

http://localhost:8000
How to Run (Local, without Docker)

1. Create a virtual environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

2. Install dependencies

pip install -r backend/requirements.txt

3. Start the backend

uvicorn app.main:app --reload

4. Open in browser

http://localhost:8000


##How It Works (High Level)##

1. User uploads a .txt file

2. Backend:

- Validates input

- Saves document to disk

- Splits content into chunks

- Attempts to generate embeddings and index them

3. If embeddings are unavailable:

- Document is still stored and chunked

- System continues to function without crashing

4. When a question is asked:

- Relevant chunks are retrieved (if indexed)

- Answer is generated or a graceful fallback is returned

- Source document chunks are shown

##What Is Done##

Document upload with validation

Chunking and persistence

Indexed document listing

Question endpoint with robust error handling

Graceful degradation when OpenAI quota is unavailable

Frontend–backend integration

Dockerized setup

Status endpoint for backend health

Clear separation of concerns in codebase

##What Is Not Done (By Design)##

No authentication or user accounts

No support for non-text files (PDF, DOCX, etc.)

No advanced UI framework (kept intentionally minimal)

No background re-indexing jobs

No production-grade caching or rate limiting

No paid API credits included (OpenAI usage is optional)
