from models.exceptions import SFMShopException, ValidationError
from models.order import Order
from models.payment import CardPayment, PayPalPayment
from models.product import Product
from models.user import User

def process_order_system():
    try:
        user = User("Иван", "ivan@test.com")
        product1 = Product("Ноутбук", 50000, 2)
        product2 = Product("Мышь", 1500, 3)
        order = Order(user, [product1, product2])

        total = order.calculate_total()
        print(f"Общая стоимость заказа: {total}")

        payments = [
            CardPayment(1000, "1234 5678 9012 3456"),
            PayPalPayment(2000, "test@paypal.com"),
        ]
        for payment in payments:
            print(payment.process_payment())

        sorted_products = sorted([product1, product2])
        for product in sorted_products:
            print(product)

    except SFMShopException as e:
        print(f"Ошибка проекта: {e}")

    try:
        product1.set_price(-1000)
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")

process_order_system()