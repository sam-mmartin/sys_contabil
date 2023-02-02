import datetime
from flaskr.models.operation import Operation
from flaskr.sqlite import get_db


class OperationRepository:

    def __init__(self) -> None:
        self.db = get_db()

    def list_all(self):
        operations: list[Operation] = self.db.execute(
            'SELECT * FROM operation'
        ).fetchall()

        return operations

    def list_by_description(self, description):
        operation = self.db.execute(
            'SELECT * FROM operation WHERE description = ?',
            (description,)
        ).fetchone()

        return operation

    def create(self, description):
        today = datetime.date.today()

        self.db.execute(
            'INSERT INTO operation (description, date_create, date_update)'
            ' VALUES (?, ?, ?)',
            (description, today, today)
        )

        self.db.commit()
