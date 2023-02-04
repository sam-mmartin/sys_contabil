from flaskr.models.annual_sums import AnnualSums
from flaskr.sqlite import get_db

import datetime


class AnnualSumsRepository:

    def __init__(self) -> None:
        self.db = get_db()

    def create(self, sum, operation_id, month, year, user_id):
        today = datetime.date.today()

        self.db.execute(
            'INSERT INTO sum_anual (amount, month, year, date_create, date_update, operation_id, user_id)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?)',
            (sum,
             month,
             year,
             today,
             today,
             operation_id,
             user_id)
        )
        self.db.commit()

    def list_by_user(self, user_id):
        today = datetime.date.today()

        sums = self.db.execute(
            'SELECT * FROM sum_anual WHERE year = ? AND user_id = ?',
            (today.year, user_id)
        ).fetchall()

        return sums

    def list_by_operation_and_user(self, operation_id, user_id):
        today = datetime.date.today()

        amount = self.db.execute(
            'SELECT * FROM sum_anual'
            ' WHERE operation_id = ? AND user_id = ? AND year = ?',
            (operation_id, user_id, today.year)
        ).fetchall()

        return self.parse(amount)

    def parse(self, rows):
        res = []

        for row in rows:
            item = AnnualSums(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )
            res.append(item)

        return res
