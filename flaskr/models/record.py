import datetime


class Record:
    id: int = 0
    description: str = ""
    value: float = 0.0
    category: str = ""
    operation: str = ""
    date: datetime.date = datetime.date.today()

    def __init__(self, description, value, category, operation, date) -> None:
        self.description = description
        self.value = value
        self.category = category
        self.operation = operation
        self.date = date

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def get_category(self):
        return self.category

    def get_operation(self):
        return self.operation

    def get_date(self):
        return self.date

    def set_id(self, id):
        self.id = id

    def set_description(self, description):
        self.description = description

    def set_value(self, value):
        self.value = value

    def set_category(self, category):
        self.category = category

    def set_operation(self, operation):
        self.operation = operation

    def set_date(self, date):
        self.date = date
