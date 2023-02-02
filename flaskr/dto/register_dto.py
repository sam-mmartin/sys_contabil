class RegisterDTO:

    def __init__(self, description, amount, date_register, category, operation) -> None:
        self.description = description
        self.amount = amount
        self.date_register = date_register
        self.category = category
        self.operation = operation
