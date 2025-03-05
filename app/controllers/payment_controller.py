from fastapi import APIRouter, HTTPException
from app.services.payment_service import PaymentService
from models.payment import Payment

router = APIRouter()

@router.post("/pay")
def create_payment(amount: int, currency: str, seller_account: str):
    """
    Cria um pagamento para um vendedor específico.

    Esta função processa o pagamento de um valor específico, em uma moeda especificada, para um vendedor
    usando a conta fornecida. O pagamento é processado através do serviço `PaymentService`.

    Parâmetros:
    - amount (int): O valor do pagamento a ser processado (em centavos).
    - currency (str): A moeda na qual o pagamento será feito, por exemplo, "USD" ou "BRL".
    - seller_account (str): Identificador da conta do vendedor que receberá o pagamento.

    Retorna:
    - dict: Um dicionário contendo o `client_secret` gerado para a transação, que é necessário para
      finalizar o pagamento do lado do cliente.
    """
    payment = Payment(amount, currency, seller_account)
    client_secret = PaymentService.process_payment(payment)
    return {"client_secret": client_secret}

@router.post("/transfer")
def transfer_payment(payment_intent_id: str, seller_account: str, amount: int):
    """
    Realiza a transferência de fundos para o vendedor.

    Esta função transfere fundos de um pagamento previamente criado para a conta do vendedor. Utiliza
    o `payment_intent_id` para identificar a transação, transferindo o valor especificado para a conta
    fornecida.

    Parâmetros:
    - payment_intent_id (str): Identificador da intenção de pagamento gerada durante o processo de pagamento.
    - seller_account (str): Identificador da conta do vendedor para onde os fundos serão transferidos.
    - amount (int): O valor a ser transferido (em centavos).

    Retorna:
    - dict: Um dicionário contendo o `transfer_id` da transferência realizada e o `status` da operação.
    """
    transfer = PaymentService.transfer_funds(payment_intent_id, seller_account, amount)
    return {"transfer_id": transfer.id, "status": transfer.status}
