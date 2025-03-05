class Payment:
    """
    Representa um pagamento a ser processado.

    A classe Payment é usada para criar uma representação de um pagamento que será realizado,
    contendo informações sobre o valor, a moeda e a conta do vendedor.

    Atributos:
    - amount (int): O valor do pagamento (em centavos).
    - currency (str): A moeda em que o pagamento será feito, como "USD" ou "BRL".
    - seller_account (str): O identificador da conta do vendedor que receberá o pagamento.
    """

    def __init__(self, amount: int, currency: str, seller_account: str):
        """
        Inicializa um objeto Payment com os dados necessários para processar o pagamento.

        Parâmetros:
        - amount (int): O valor do pagamento a ser realizado (em centavos).
        - currency (str): A moeda em que o pagamento será feito, como "USD" ou "BRL".
        - seller_account (str): O identificador da conta do vendedor que receberá o pagamento.
        """
        self.amount = amount
        self.currency = currency
        self.seller_account = seller_account
