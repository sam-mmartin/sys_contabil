class RegisterDTO:

    def __init__(self, id, description, amount, date_register, category, operation) -> None:
        self.id = id
        self.description = description
        self.amount = amount
        self.date_register = date_register
        self.category = category
        self.operation = operation
