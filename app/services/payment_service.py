import stripe
from fastapi import HTTPException
from app.models.payment import Payment

class PaymentService:
    """
    Serviço responsável pelo processamento de pagamentos e transferências.

    Esta classe contém métodos estáticos para realizar o processamento de pagamentos e transferências
    de fundos utilizando a API Stripe. Os métodos lidam com a criação de intenções de pagamento e a
    transferência de fundos após a dedução da comissão.

    Métodos:
    - process_payment: Cria uma intenção de pagamento usando a API Stripe.
    - transfer_funds: Realiza a transferência de fundos para o vendedor após a dedução da comissão.
    """

    @staticmethod
    def process_payment(payment: Payment):
        """
        Processa o pagamento e cria uma intenção de pagamento com o Stripe.

        Este método utiliza a API Stripe para criar uma intenção de pagamento, especificando o valor,
        a moeda e o método de pagamento (cartão). Retorna o `client_secret` da intenção de pagamento,
        que é necessário para completar o pagamento do lado do cliente.

        Parâmetros:
        - payment (Payment): O objeto Payment contendo as informações do pagamento.

        Retorna:
        - str: O `client_secret` gerado pela Stripe para completar o pagamento no lado do cliente.

        Lança:
        - HTTPException: Se ocorrer algum erro durante o processo de criação da intenção de pagamento.
        """
        try:
            intent = stripe.PaymentIntent.create(
                amount=payment.amount,
                currency=payment.currency,
                payment_method_types=["card"],
                capture_method="automatic",
            )
            return intent.client_secret
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def transfer_funds(payment_intent_id: str, seller_account: str, amount: int):
        """
        Realiza a transferência de fundos para o vendedor após a dedução de comissão.

        Este método realiza a transferência de uma parte do pagamento (após deduzir uma comissão de 15%)
        para a conta do vendedor usando a API Stripe.

        Parâmetros:
        - payment_intent_id (str): O ID da intenção de pagamento que originou a transação.
        - seller_account (str): O identificador da conta do vendedor que receberá os fundos.
        - amount (int): O valor total a ser transferido (em centavos).

        Retorna:
        - stripe.Transfer: O objeto de transferência gerado pela API Stripe.

        Lança:
        - HTTPException: Se ocorrer algum erro durante o processo de transferência.
        """
        try:
            commission = int(amount * 0.15)
            seller_amount = amount - commission

            transfer = stripe.Transfer.create(
                amount=seller_amount,
                currency="usd",
                destination=seller_account,
                source_transaction=payment_intent_id,
            )
            return transfer
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
