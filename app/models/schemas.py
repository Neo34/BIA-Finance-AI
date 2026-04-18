from pydantic import BaseModel

class PerguntaRequest(BaseModel):
    pergunta: str

class SimulacaoRequest(BaseModel):
    valor: float
    taxa: float
    meses: int