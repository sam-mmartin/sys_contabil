from datetime import datetime
from functools import reduce
from flaskr.models.annual_sums import AnnualSums
from flaskr.repository.annual_sums_repository import AnnualSumsRepository
from flaskr.services.register_service import RegisterService


class AnnualSumsService:

    def __init__(self, repository: AnnualSumsRepository,
                 reg_serv: RegisterService) -> None:
        self.repository = repository
        self.reg_serv = reg_serv

    def set_sum_month(self, operation_id, month, year, user_id):
        sum = self.reg_serv.get_sum_amount(operation_id, month, user_id)

        if_exists = self.repository.if_exists(
            month, year, operation_id, user_id)

        if if_exists is not None:
            self.repository.update(if_exists[0], sum)
        else:
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

    def get_all_annual_sums_by_months(self, user_id):
        annual_sums = self.repository.list_by_user(user_id)
        sums_dict = {}

        months = reduce(
            lambda reg, x: reg +
            [x.month] if x.month not in reg else reg,
            annual_sums,
            []
        )

        for m in months:
            sums = list(filter(
                lambda item: item.month == m, annual_sums
            ))

            res = {}
            for s in sums:
                month = self.get_month_name(s)
                res[s.operation_id] = s.amount

            sums_dict[month] = res

        return sums_dict

    def get_month_name(self, item):
        month = datetime(item.year, item.month, 1).strftime('%b')
        return month
