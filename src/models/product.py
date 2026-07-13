from models.exceptions import InsufficientStockError, InvalidQuantityError, ValidationError

class Product:

    def __init__(self, name, price, quantity, stock=100) -> None:
        self.name = name

        self.set_price(price)
        self.quantity = quantity
        self.stock = stock

    def set_price(self, value):
        if value < 0:
            raise ValidationError("Цена не может быть отрицательной")
        self.price = value

    def get_total_price(self):
        return self.price * self.quantity

    def sell(self, amount):
        if amount <= 0:
            raise InvalidQuantityError(
                f"Количество должно быть больше нуля, получено {amount}"
            )
        if self.stock < amount:
            raise InsufficientStockError(
                f"Товара недостаточно. На складе {self.stock}, требуется {amount}"
            )
        else:
            self.stock -= amount
            print(
                f"Продано {amount} шт. товара {self.name}. Остаток {self.stock}"
            )

    def __str__(self) -> str:
        return f"Товар: {self.name}, Цена {self.price} руб., Количество {self.quantity}"

    def __repr__(self) -> str:
        return f"Product('{self.name}', '{self.price}', '{self.quantity}')"

    def __lt__(self, other):
        if not isinstance(other, Product):
            raise NotImplemented
        return self.price < other.price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            raise NotImplemented
        return all(
            [self.name == other.name, self.price == other.price]
        )