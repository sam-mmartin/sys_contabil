class Operation:

    def __init__(self, id, description, date_create, date_update) -> None:
        self.id = id
        self.description = description
        self.date_create = date_create
        self.date_update = date_update

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def get_date_create(self):
        return self.date_create

    def get_date_update(self):
        return self.date_update

    def set_id(self, id):
        self.id = id

    def set_description(self, description):
        self.description = description

    def set_date_create(self, date_create):
        self.date_create = date_create

    def set_date_update(self, date_update):
        self.date_update = date_update
