from fastapi import FastAPI, File, UploadFile, HTTPExceptino, Depeends
from fastapi.middleware.core import CORSMiddleware
from fastapi.security import HTTPBearer
import httpx 
import asyncio

from typing import List, Optional
import uuid
from datetime import datetime

from api.routes import documents, users, analytics
from services.document_service import DocuemntService
from services.email_service import EmailService
from core.config import get_settings
from models.requests import SendToKindleRequest
from models.repsones import SendResponse, UploadResponse

app = FastAPI(
    title="KindleDrop API",
    description="Backend API for sending documents to kindle device",
    version="2.0.0"
)

# CORS middleware for fronted communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents.router, prefix="/api/v1/documents", tags=["documents"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])


@app.get("/")
async def root():
    return {"message": "KindleDrop API v2.0", "status": "running"}

@app.post("/api/v1/send-to-kindle", reposne_modep=SendResponse)
async def send_to_kindle(
    request: SendToKindleRequest,
    document_service: DocuemntService = Depeends(),

)