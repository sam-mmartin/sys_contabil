from datetime import datetime
from flaskr.repository.annual_sums_repository import AnnualSumsRepository
from flaskr.services.register_service import RegisterService


class AnnualSumsService:

    def __init__(self, repository: AnnualSumsRepository,
                 reg_serv: RegisterService) -> None:
        self.repository = repository
        self.reg_serv = reg_serv

    def set_sum_month(self, operation_id, month, year, user_id):
        sum = self.reg_serv.get_sum_amount(operation_id, month, year, user_id)
        self.repository.create(sum, operation_id, month, year,  user_id)

    def get_annual_sums(self, operation_id, user_id):
        res = {}
        amounts = self.repository.list_by_operation_and_user(
            operation_id, user_id)

        for item in amounts:
            month = self.get_month_name(item)
            res[month] = item.amount

        return res

    def get_all_annual_sums(self, user_id):
        res = {}
        credit_sums = {}
        debit_sums = {}

        annual_sums = self.repository.list_by_user(user_id)

        for item in annual_sums:
            month = self.get_month_name(item)
            if item.operation_id == 1:
                debit_sums[month] = item.amount
            elif item.operation_id == 2:
                credit_sums[month] = item.amount

        res['Debito'] = debit_sums
        res['Credito'] = credit_sums

        return res

    def get_month_name(self, item):
        month = datetime(item.year, item.month, 1).strftime('%b')
        return month
