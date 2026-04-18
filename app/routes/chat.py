from fastapi import APIRouter
from app.models.schemas import PerguntaRequest
from app.services.bia_service import responder

router = APIRouter()

@router.post("/chat")
def chat(req: PerguntaRequest):
    resposta = responder(req.pergunta)
    return {"resposta": resposta}git add app/routes/chat.py