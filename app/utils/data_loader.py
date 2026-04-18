import pandas as pd
import json

def carregar_dados():
    transacoes = pd.read_csv("app/data/transacoes.csv")

    with open("app/data/perfil_investidor.json") as f:
        perfil = json.load(f)

    with open("app/data/produtos_financeiros.json") as f:
        produtos = json.load(f)

    return transacoes, perfil, produtos