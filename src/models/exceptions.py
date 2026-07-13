class SFMShopException(Exception):
    pass

class ValidationError(SFMShopException):
    pass

class BusinessLogicError(SFMShopException):
    pass

class InsufficientStockError(BusinessLogicError):
    pass

class InvalidOrderError(BusinessLogicError):
    pass

class InvalidQuantityError(BusinessLogicError):
    pass

class DatabaseError(SFMShopException):
    pass