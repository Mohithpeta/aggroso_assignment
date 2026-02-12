from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.api import status
from app.api import status, upload, documents
from app.api import status, upload, documents, qa

from fastapi.staticfiles import StaticFiles





app = FastAPI(title="Private Knowledge Q&A")

app.include_router(status.router)
app.include_router(status.router)
app.include_router(upload.router)
app.include_router(documents.router)
app.include_router(status.router)
app.include_router(upload.router)
app.include_router(documents.router)
app.include_router(qa.router)



    
app.mount(
    "/",
    StaticFiles(directory="app/static", html=True),
    name="static",
)