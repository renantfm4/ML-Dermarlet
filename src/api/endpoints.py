# Pequena endpoint para testar, mas deverá ser removida
from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "pong"}
