# 🧠 BIA Finance AI

### Assistente Financeira Inteligente com IA Generativa

---

## 📌 Sobre o Projeto

O **BIA Finance AI** é uma assistente virtual inteligente focada em relacionamento financeiro, desenvolvida com **Python, IA generativa e análise de dados**.

A aplicação simula uma experiência real de atendimento digital, sendo capaz de:

* Compreender linguagem natural
* Responder perguntas financeiras com contexto
* Analisar gastos do usuário
* Sugerir produtos financeiros
* Realizar simulações de investimento
* Manter histórico de interação

Este projeto foi desenvolvido como parte de um desafio prático com foco em **IA aplicada, UX e dados**, consolidando conhecimentos modernos utilizados no mercado.

---

## 🚀 Funcionalidades

### 💬 Atendimento Inteligente

* Interpretação de perguntas em linguagem natural
* Respostas personalizadas com base no perfil do usuário

### 📊 Análise Financeira

* Leitura de transações financeiras (CSV)
* Identificação de padrões de gastos
* Agrupamento por categoria

### 💰 Simulação de Investimentos

* Cálculo de rendimento com base em taxa e tempo
* Sugestões alinhadas ao perfil do investidor

### 🧠 Contexto e Memória

* Histórico de interações
* Respostas mais coerentes e contextualizadas

### 📦 Integração com Dados

* Perfil do investidor (JSON)
* Produtos financeiros disponíveis
* Histórico de atendimentos

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* OpenAI API
* JSON / CSV
* (Opcional) FastAPI / Flask
* (Opcional) Streamlit

---

## 📂 Estrutura do Projeto

```
bia-finance-ai/
│
├── data/
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   └── produtos_financeiros.json
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/bia-finance-ai.git
cd bia-finance-ai
```

---

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure a API Key

Crie um arquivo `.env`:

```
OPENAI_API_KEY=sua_chave_aqui
```

---

### 5. Execute a aplicação

```bash
python app.py
```

---

## 💡 Exemplos de Uso

```bash
Você: Quanto eu gasto por mês?
BIA: Com base nos seus dados, seus maiores gastos estão em alimentação e transporte...

Você: Vale a pena investir em CDB?
BIA: Considerando seu perfil conservador, o CDB é uma boa opção...

Você: Simule um investimento de 1000 reais por 12 meses
BIA: O valor estimado ao final do período seria...
```

---

## 🧠 Diferenciais do Projeto

* Uso de IA generativa com contexto real
* Integração com dados estruturados
* Foco em experiência do usuário (UX)
* Simulação de cenário real de mercado financeiro
* Arquitetura simples e escalável

---

## 📈 Possíveis Melhorias Futuras

* Interface web interativa (Streamlit ou React)
* API REST com FastAPI
* Autenticação de usuário
* Dashboard financeiro
* Integração com bancos (Open Finance)
* Machine Learning para previsões financeiras

---

## 👨‍💻 Autor

Desenvolvido por **Cesar Constanzo**



---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## ⭐ Contribuição

Sinta-se à vontade para contribuir com melhorias, sugestões ou novas funcionalidades.

---

## 🚀 Status do Projeto

✅ Em desenvolvimento ativo
🔥 Pronto para evoluir para nível profissional

---
