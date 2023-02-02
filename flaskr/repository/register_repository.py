from calendar import monthrange
import datetime

from flaskr.dto.register_request_dto import RegisterRequestDto
from flaskr.sqlite import get_db


class RegisterRepository:

    def __init__(self) -> None:
        self.db = get_db()

    def list_registers_by_operation(self, operation_id):
        registers = self.db.execute(
            'SELECT r.description, r.amount, r.date_register, cat.description, op.description'
            ' FROM register r'
            ' JOIN category cat ON r.category_id = cat.id'
            ' JOIN operation op ON r.operation_id = op.id'
            ' JOIN user u ON r.user_id = u.id'
            ' WHERE op.id = ?'
            ' ORDER BY r.date_register DESC',
            (operation_id,)
        ).fetchall()

        return registers

    def list_registers_by_category(self, operation_id, category_id):
        registers = self.db.execute(
            'SELECT r.description, r.amount, r.date_register, cat.description, op.description'
            ' FROM register r'
            ' JOIN category cat ON r.category_id = cat.id'
            ' JOIN operation op ON r.operation_id = op.id'
            ' JOIN user u ON r.user_id = u.id'
            ' WHERE op.id = ? AND cat.id = ?'
            ' ORDER BY r.date_register DESC',
            (operation_id, category_id,)
        ).fetchall()

        return registers

    def create(self, register: RegisterRequestDto):
        today = datetime.date.today()

        self.db.execute(
            'INSERT INTO register (description, amount, operation_id, category_id, date_register, date_update, user_id)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?)',
            (register.description,
             register.amount,
             register.operation,
             register.category,
             register.date_register,
             today,
             register.user_id)
        )
        self.db.commit()

    def select_sum_amount(self, operation_id, month):
        sum = 0

        if month:
            today = datetime.date.today()
            first_day = datetime.date(today.year, today.month, 1)
            last_day = datetime.date(today.year, today.month,
                                     monthrange(today.year, today.month)[1])

            sum = self.db.execute(
                'SELECT SUM(amount) FROM register'
                ' WHERE operation_id = ? AND date_register BETWEEN ? AND ?',
                (operation_id, first_day, last_day)
            ).fetchone()
        else:
            sum = self.db.execute(
                'SELECT SUM(amount) FROM register WHERE operation_id = ?',
                (operation_id,)
            ).fetchone()

        return sum[0]

    def select_count_registers(self, operation_id):
        count = self.db.execute(
            'SELECT COUNT(id) FROM register WHERE operation_id = ?',
            (operation_id,)
        ).fetchone()

        return count[0]

    def create_credit_sum_annual(self, sum, month, year, user_id):
        today = datetime.date.today()

        self.db.execute(
            'INSERT INTO sum_credit_anual (credit_amount, credit_month, credit_year, date_create, date_update, user_id'
            ' VALUES (?, ?, ?, ?, ?, ?)',
            (sum, month, year, today, today, user_id)
        )
        self.db.commit()
