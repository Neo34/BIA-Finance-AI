from fastapi import APIRouter
from app.models.schemas import SimulacaoRequest
from app.utils.data_loader import carregar_dados

router = APIRouter()

@router.get("/gastos")
def gastos():
    transacoes, _, _ = carregar_dados()
    resumo = transacoes.groupby("categoria")["valor"].sum().to_dict()
    return {"gastos": resumo}


@router.post("/simulacao")
def simulacao(req: SimulacaoRequest):
    resultado = req.valor * (1 + req.taxa) ** req.meses
    return {"resultado": round(resultado, 2)}