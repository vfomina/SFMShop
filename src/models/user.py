from models.exceptions import ValidationError

class User:

    def __init__(self, name, email):
        self.name = name
        self.set_email(email)

    def set_email(self, value):
        if ("@" or '.') not in value:
            raise ValidationError("Неверный формат email")
        self.email = value

    def get_info(self):
        return f"Пользователь: {self.name}, Email: {self.email}"
