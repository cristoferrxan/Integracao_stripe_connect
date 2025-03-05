from fastapi import FastAPI
from app.controllers.payment_controller import router as payment_router

app = FastAPI()

# Registrar as rotas
app.include_router(payment_router)

@app.get("/")
def root():
    """
    Endpoint raiz da API.

    Este endpoint retorna uma mensagem simples para indicar que a API está em funcionamento.
    Ele serve como um ponto de verificação para garantir que o servidor está ativo.

    Retorna:
    - dict: Um dicionário com uma chave `message` que contém a mensagem "Stripe Integration API is running!".
    """
    return {"message": "Stripe Integration API is running!"}
