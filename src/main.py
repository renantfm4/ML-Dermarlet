from fastapi import FastAPI
from src.api.endpoints import router as api_router

app = FastAPI(title="Pre-Diagnostic ML Service")
app.include_router(api_router, prefix="/api")