from datetime import datetime
from flaskr.dto.register_dto import RegisterDTO

from flaskr.dto.register_request_dto import RegisterRequestDto
from flaskr.repository.category_repository import CategoryRepository
from flaskr.repository.operation_repository import OperationRepository
from flaskr.repository.register_repository import RegisterRepository

import numpy as np


class RegisterService:

    def __init__(self, repository: RegisterRepository, op_repo: OperationRepository, cat_repo: CategoryRepository) -> None:
        self.repository = repository
        self.op_repo = op_repo
        self.cat_repo = cat_repo

    def list_all_registers_by_operation(self, operation_id):
        registers = self.repository.list_registers_by_operation(operation_id)
        return self.list_registers(registers)

    def list_all_registers_by_category(self, operation_id, category_id):
        registers = self.repository.list_registers_by_category(
            operation_id, category_id)
        return self.list_registers(registers)

    def list_registers(self, registers):
        res: list[RegisterDTO] = []

        for register in registers:
            res.append(RegisterDTO(
                register[0], register[1], register[2], register[3], register[4]
            ))

        return res

    def create_register(self, description, amount, category, operation, date_register, user_id):
        date = datetime.strptime(date_register, '%d-%m-%Y').date()

        op = self.op_repo.list_by_description(operation)
        cat = self.cat_repo.list_by_description(category)

        register = RegisterRequestDto(
            description, amount, cat['id'], op['id'], date, user_id
        )

        self.repository.create(register)

    def get_sum_amount(self, operation_id, month):
        return self.repository.select_sum_amount(operation_id, month)

    def month_debits_sum_amount(self):
        registers = self.list_all_registers_by_operation(1)
        dates = self.return_dates_month_debits(registers)
        res = {}
        sum = 0

        dates.sort()

        for day in dates:
            for item in registers:
                if item.date_register.day == day:
                    sum += item.amount

            res[day] = sum
            sum = 0

        return res

    def return_dates_month_debits(self, debits: list[RegisterDTO]):
        dates = []

        for item in debits:
            if not dates.__contains__(item.date_register.day):
                dates.append(item.date_register.day)

        return dates

    def invoice_debits(self) -> dict:
        invoice_dict = {}
        categorys = self.cat_repo.list_all()

        for category in categorys:
            debits = self.list_all_registers_by_category(1, category.id)
            sum_amount = self.calc(debits)
            invoice_dict[category.description] = sum_amount

        return invoice_dict

    def calc(self, registers: list[RegisterDTO]):
        values = []

        for item in registers:
            values.append(item.amount)

        res = np.sum(np.asarray(values, dtype=float))
        return res

    def count_registers_by_operation(self, operation_id):
        return self.repository.select_count_registers(operation_id)

    def set_credit_sum_month(self, month, year, user_id):
        sum = self.get_sum_amount(2, False)
        self.repository.create_credit_sum_annual(sum, month, year, user_id)
