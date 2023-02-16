from calendar import monthrange
from datetime import datetime
from flaskr.dto.register_dto import RegisterDTO

from flaskr.dto.register_request_dto import RegisterRequestDto
from flaskr.repository.category_repository import CategoryRepository
from flaskr.repository.operation_repository import OperationRepository
from flaskr.repository.register_repository import RegisterRepository

import numpy as np


class RegisterService:

    def __init__(self, repository: RegisterRepository,
                 op_repo: OperationRepository,
                 cat_repo: CategoryRepository) -> None:
        self.repository = repository
        self.op_repo = op_repo
        self.cat_repo = cat_repo
        self.year = datetime.now().year

    def list_all_registers_by_operation(self, operation_id, month, user_id):
        dt = self.get_first_and_last_day_to_month(month)
        registers = self.repository.list_registers_by_operation(
            operation_id, dt, user_id)
        return self.mapper_list_to_dto(registers)

    def list_all_registers_by_category(self, operation_id, category_id, month, user_id):
        dt = self.get_first_and_last_day_to_month(month)
        registers = self.repository.list_registers_by_category(
            operation_id, category_id, dt, user_id)
        return self.mapper_list_to_dto(registers)

    def get_register_by_id(self, id, user_id):
        register = self.repository.get_by_id(id, user_id)
        return self.mapper_to_dto(register)

    def mapper_to_dto(self, register):
        res = RegisterDTO(
            register[0], register[1], register[2], register[3], register[4], register[5]
        )

        return res

    def mapper_list_to_dto(self, registers):
        res: list[RegisterDTO] = []

        for register in registers:
            res.append(self.mapper_to_dto(register))

        return res

    def create_register(self, description, amount, category, operation, date_register, user_id):
        date = datetime.strptime(date_register, '%d-%m-%Y').date()

        op = self.op_repo.list_by_description(operation)
        cat = self.cat_repo.list_by_description(category)

        register = RegisterRequestDto(
            description, amount, cat['id'], op['id'], date, user_id
        )

        self.repository.create(register)

    def update_register(self, id, description, amount, category, operation, date_register, user_id):
        date = datetime.strptime(date_register, '%d-%m-%Y').date()

        op = self.op_repo.list_by_description(operation)
        cat = self.cat_repo.list_by_description(category)

        register = RegisterRequestDto(
            description, amount, cat['id'], op['id'], date, user_id
        )

        self.repository.update(id, register)

    def get_sum_amount(self, operation_id, month, user_id):
        dt = self.get_first_and_last_day_to_month(month)
        sum = self.repository.select_sum_amount(operation_id, dt, user_id)

        if sum is None:
            sum = 0

        return round(sum, 2)

    def month_debits_sum_amount(self, month, user_id):
        registers = self.list_all_registers_by_operation(1, month, user_id)
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

    def invoice_debits(self, month, user_id) -> dict:
        invoice_dict = {}
        categorys = self.cat_repo.list_all()

        for category in categorys:
            debits = self.list_all_registers_by_category(
                1, category.id, month, user_id)
            sum_amount = self.calc(debits)
            invoice_dict[category.description] = sum_amount

        return invoice_dict

    def calc(self, registers: list[RegisterDTO]):
        values = []

        for item in registers:
            values.append(item.amount)

        res = np.sum(np.asarray(values, dtype=float))
        return res

    def count_registers_by_operation(self, operation_id, month, user_id):
        dt = self.get_first_and_last_day_to_month(month)
        return self.repository.select_count_registers(operation_id, dt, user_id)

    def get_first_and_last_day_to_month(self, month):
        first_day = datetime(self.year, month, 1).date()
        last_day = datetime(self.year, month,
                            monthrange(self.year, month)[1]).date()

        res = {
            "first_day": first_day,
            "last_day": last_day
        }

        return res

    def delete(self, id, user_id):
        self.repository.delete(id, user_id)
