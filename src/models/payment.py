class Payment:

    def __init__(self, amount) -> None:
        self.amount = amount

    def process_payment(self):
        raise NotImplementedError("Метод должен быть переопределен")

class CardPayment(Payment):

    def __init__(self, amount, card_number) -> None:
        super().__init__(amount)
        self.__card_number = card_number

    def process_payment(self):
        masked_card = "****" + self.__card_number[-4:]
        return f"Оплата картой {masked_card}: {self.amount} руб."

class PayPalPayment(Payment):

    def __init__(self, amount, email) -> None:
        super().__init__(amount)
        self._email = email

    def get_email(self):
        return self._email

    def process_payment(self):
        return f"Оплата PayPal {self._email}: {self.amount} руб."