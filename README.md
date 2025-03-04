
# Stripe Integration API

Este projeto tem como objetivo integrar a API da **Stripe** com um backend desenvolvido utilizando **FastAPI**. A API permite o processamento de pagamentos e a transferência de fundos para vendedores, utilizando o serviço de pagamentos da Stripe.

```

## Pré-requisitos

Antes de rodar o projeto, é necessário ter o seguinte instalado:

- **Python 3.7+**
- **Stripe API Key** (Você pode obter a chave secreta no [dashboard da Stripe](https://dashboard.stripe.com))

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/stripe-integration-api.git
   cd stripe-integration-api
   ```

2. **Crie um ambiente virtual e ative-o** (recomendado):

   - No Windows:
     ```bash
     python -m venv venv
     venv\Scripts\Activate
     ```

   - No macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:

   Crie um arquivo `.env` na raiz do projeto e adicione a chave secreta da Stripe:

   ```bash
   STRIPE_SECRET_KEY=your_stripe_secret_key
   ```

## Como Rodar

1. **Execute o servidor FastAPI**:

   Com as dependências instaladas e a chave da Stripe configurada, execute o seguinte comando para iniciar a aplicação:

   ```bash
   uvicorn app.main:app --reload
   ```

   O servidor estará rodando em `http://127.0.0.1:8000`.

2. **Endpoints Disponíveis**:

   - `POST /pay`: Processa um pagamento.
   - `POST /transfer`: Realiza a transferência de fundos para o vendedor.

   Você pode verificar o status da API acessando `http://127.0.0.1:8000/`.

## Exemplos de Requisição

### Processar Pagamento

- **Endpoint**: `/pay`
- **Método**: `POST`
- **Corpo da Requisição**:

  ```json
  {
    "amount": 5000,
    "currency": "usd",
    "seller_account": "acct_1GqH6R2eZvKvN4Wx"
  }
  ```

- **Resposta**:

  ```json
  {
    "client_secret": "pi_1GqH6R2eZvKvN4Wx_secret_MySecretKey"
  }
  ```

### Transferir Fundos

- **Endpoint**: `/transfer`
- **Método**: `POST`
- **Corpo da Requisição**:

  ```json
  {
    "payment_intent_id": "pi_1GqH6R2eZvKvN4Wx",
    "seller_account": "acct_1GqH6R2eZvKvN4Wx",
    "amount": 5000
  }
  ```

- **Resposta**:

  ```json
  {
    "transfer_id": "tr_1GqH7R2eZvKvN4Wx",
    "status": "succeeded"
  }
  ```

## Dependências

O projeto utiliza as seguintes dependências:

- `FastAPI`: Framework para a criação da API.
- `stripe`: SDK para integração com a API Stripe.
- `python-dotenv`: Carregar variáveis de ambiente a partir de um arquivo `.env`.
- `uvicorn`: Servidor ASGI para rodar a aplicação FastAPI.

## Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
