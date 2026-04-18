from fastapi import FastAPI
from app.routes import chat, finance

app = FastAPI(title="BIA Finance AI")

app.include_router(chat.router)
app.include_router(finance.router)