import datetime


class Register:
    def __init__(self, id, description, amount, category_id, operation_id, date_register, user_id, date_update) -> None:
        self.id = id
        self.description = description
        self.amount = amount
        self.category_id = category_id
        self.operation_id = operation_id
        self.date_register = date_register
        self.date_update = date_update
        self.user_id = user_id

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def get_amount(self):
        return self.amount

    def get_category_id(self):
        return self.category_id

    def get_operation_id(self):
        return self.operation_id

    def get_date_register(self):
        return self.date_register

    def get_date_update(self):
        return self.date_update

    def get_user_id(self):
        return self.user_id

    def set_id(self, id):
        self.id = id

    def set_description(self, description):
        self.description = description

    def set_amount(self, amount):
        self.amount = amount

    def set_category_id(self, category_id):
        self.category_id = category_id

    def set_operation_id(self, operation_id):
        self.operation_id = operation_id

    def set_date_register(self, date_register):
        self.date_register = date_register

    def set_date_update(self, date_update):
        self.date_update = date_update

    def set_user_id(self, user_id):
        self.user_id = user_id
