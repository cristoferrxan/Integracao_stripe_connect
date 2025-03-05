import os
from dotenv import load_dotenv
import stripe

# Carregar variáveis de ambiente
load_dotenv()

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
stripe.api_key = STRIPE_SECRET_KEY

"""
Configura a integração com a Stripe carregando a chave secreta da API.

Este código carrega as variáveis de ambiente a partir de um arquivo `.env` e configura a chave secreta
da API da Stripe, permitindo a interação com os serviços de pagamento da plataforma.

Passos realizados:
1. Carrega as variáveis de ambiente usando a função `load_dotenv()`.
2. Recupera a chave secreta da Stripe da variável de ambiente `STRIPE_SECRET_KEY`.
3. Define a chave da API da Stripe com a chave recuperada, autorizando a utilização da API.

Certifique-se de que a chave `STRIPE_SECRET_KEY` esteja corretamente configurada no arquivo `.env`.
"""
