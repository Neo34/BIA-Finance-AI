from openai import OpenAI
from app.utils.data_loader import carregar_dados

client = OpenAI()

historico = []

def gerar_contexto(pergunta):
    transacoes, perfil, produtos = carregar_dados()

    gastos_totais = transacoes["valor"].sum()

    contexto = f"""
    Você é uma assistente financeira inteligente.

    Perfil do cliente:
    {perfil}

    Gastos totais:
    R$ {gastos_totais}

    Produtos disponíveis:
    {produtos}

    Histórico:
    {historico}

    Pergunta:
    {pergunta}
    """

    return contexto


def responder(pergunta):
    historico.append(pergunta)

    contexto = gerar_contexto(pergunta)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Você é uma BIA financeira especialista."},
            {"role": "user", "content": contexto}
        ]
    )

    return response.choices[0].message.content