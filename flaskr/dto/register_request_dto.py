class RegisterRequestDto:

    def __init__(self, description, amount, category, operation, date_register, user_id) -> None:
        self.description = description
        self.amount = amount
        self.category = category
        self.operation = operation
        self.date_register = date_register
        self.user_id = user_id
