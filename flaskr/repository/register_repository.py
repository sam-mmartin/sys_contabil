from calendar import monthrange
import datetime

from flaskr.dto.register_request_dto import RegisterRequestDto
from flaskr.sqlite import get_db


class RegisterRepository:

   def __init__(self) -> None:
      self.db = get_db()

   def list_registers_by_operation(self, operation_id, date_reference, user_id):
      registers = self.db.execute(
          'SELECT r.id, r.description, r.amount, r.date_register, cat.description, op.description'
          ' FROM register r'
          ' JOIN category cat ON r.category_id = cat.id'
          ' JOIN operation op ON r.operation_id = op.id'
          ' JOIN user u ON r.user_id = u.id'
          ' WHERE op.id = ? AND r.user_id = ?'
          ' AND r.date_register BETWEEN ? AND ?'
          ' ORDER BY r.date_register DESC',
          (operation_id,
           user_id,
           date_reference['first_day'],
           date_reference['last_day'])
      ).fetchall()

      return registers

   def list_registers_by_category(self, operation_id, category_id, date_reference, user_id):
      registers = self.db.execute(
          'SELECT r.id, r.description, r.amount, r.date_register, cat.description, op.description'
          ' FROM register r'
          ' JOIN category cat ON r.category_id = cat.id'
          ' JOIN operation op ON r.operation_id = op.id'
          ' JOIN user u ON r.user_id = u.id'
          ' WHERE op.id = ? AND cat.id = ? AND r.user_id = ?'
          ' AND r.date_register BETWEEN ? AND ?'
          ' ORDER BY r.date_register DESC',
          (operation_id,
           category_id,
           user_id,
           date_reference['first_day'],
           date_reference['last_day'])
      ).fetchall()

      return registers

#    def list_registers_by_month(self, month, user_id):

   def get_by_id(self, id, user_id):
      register = self.db.execute(
          'SELECT r.id, r.description, r.amount, r.date_register, cat.description, op.description'
          ' FROM register r'
          ' JOIN category cat ON r.category_id = cat.id'
          ' JOIN operation op ON r.operation_id = op.id'
          ' JOIN user u ON r.user_id = u.id'
          ' WHERE r.id = ? AND r.user_id = ?',
          (id, user_id)
      ).fetchone()

      return register

   def create(self, register: RegisterRequestDto):
      today = datetime.date.today()

      self.db.execute(
          'INSERT INTO register '
          '(description,'
          'amount,'
          'operation_id,'
          'category_id,'
          'group_by_id,'
          'date_register,'
          'date_update,'
          'user_id)'
          ' VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
          (register.description,
           register.amount,
           register.operation,
           register.category,
           register.group_by,
           register.date_register,
           today,
           register.user_id)
      )
      self.db.commit()

   def update(self, id, register: RegisterRequestDto):
      today = datetime.date.today()

      self.db.execute(
          'UPDATE register SET'
          ' description = ?, amount = ?, operation_id = ?, category_id = ?, date_register = ?, date_update = ?'
          ' WHERE id = ? AND user_id = ?',
          (register.description,
           register.amount,
           register.operation,
           register.category,
           register.date_register,
           today,
           id,
           register.user_id)
      )
      self.db.commit()

   def delete(self, id, user_id):
      self.db.execute(
          'DELETE FROM register WHERE id = ? AND user_id = ?', (id, user_id)
      )
      self.db.commit()

   def select_sum_amount(self, operation_id, date_reference, user_id):
      sum = self.db.execute(
          'SELECT SUM(amount) FROM register'
          ' WHERE operation_id = ? AND user_id = ?'
          ' AND date_register BETWEEN ? AND ?',
          (operation_id,
           user_id,
           date_reference['first_day'],
           date_reference['last_day'])
      ).fetchone()

      return sum[0]

   def select_count_registers(self, operation_id, date_reference, user_id):
      count = self.db.execute(
          'SELECT COUNT(id) FROM register WHERE operation_id = ?'
          ' AND user_id = ? AND date_register BETWEEN ? AND ?',
          (operation_id,
           user_id,
           date_reference['first_day'],
           date_reference['last_day'])
      ).fetchone()

      return count[0]
