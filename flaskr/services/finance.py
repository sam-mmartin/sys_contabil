from calendar import monthrange
from datetime import date, datetime
from functools import reduce
from ..models.record import Record
from ..repository.record_repository import RecordRepository

import numpy as np


class FinanceService:

    records: list[Record] = []
    categorys = []

    def __init__(self, record_repository: RecordRepository) -> None:
        self.record_repository = record_repository
        self.records = self.record_repository.list_all()

    def get_debits(self):
        records = self.record_repository.list_all()
        debits = list(filter(
            lambda debit: debit.operation == 'Debito', records
        ))

        return debits

    def get_credits(self):
        records = self.record_repository.list_all()
        credits = list(filter(
            lambda credit: credit.operation == 'Credito', records
        ))

        return credits

    def get_credit_amount(self):
        credits = self.get_credits()
        return self.calc(credits)

    def get_debit_amount(self):
        debits = self.get_debits()
        return self.calc(debits)

    def set_categorys(self, registers):
        self.categorys = reduce(
            lambda reg, x: reg +
            [x.category] if x.category not in reg else reg,
            registers,
            []
        )

    def calc(self, list_records: list[Record]):
        values = []

        for item in list_records:
            values.append(item.value)

        res = np.sum(np.asarray(values, dtype=float))
        return res

    def list_all_month_debits(self):
        today = date.today()
        first_day = date(today.year, today.month-1, 1)
        last_day = date(today.year, today.month-1,
                        monthrange(today.year, today.month-1)[1])
        debits = self.get_debits()
        month_debits = []

        for debit in debits:
            item_date = datetime.strptime(debit.date, "%Y-%m-%d").date()

            if item_date >= first_day and item_date <= last_day:
                month_debits.append(debit)

        return month_debits

    def list_all_month_credits(self):
        today = date.today()
        first_day = date(today.year, today.month-1, 1)
        last_day = date(today.year, today.month-1,
                        monthrange(today.year, today.month)[1])
        credits = self.get_credits()
        month_credits = []

        for credit in credits:
            item_date = datetime.strptime(credit.date, "%Y-%m-%d").date()

            if item_date >= first_day and item_date <= last_day:
                month_credits.append(credit)

        return month_credits

    def list_all_month_debits_value(self):
        debits = self.list_all_month_debits()
        dates = self.return_dates_month_debits(debits)
        dates.sort()
        res = {}
        sum = 0

        for day in dates:
            for item in debits:
                item_date = datetime.strptime(item.date, "%Y-%m-%d").date()

                if item_date.day == day:
                    sum += float(item.value)

            res[day] = round(sum, 2)
            sum = 0

        return res

    def return_dates_month_debits(self, debits):
        dates = []

        for item in debits:
            item_date = datetime.strptime(item.date, "%Y-%m-%d").date()

            if not dates.__contains__(item_date.day):
                dates.append(item_date.day)

        return dates

    def invoice_debits(self) -> dict:
        invoice_dict = {}
        debits = self.get_debits()
        self.set_categorys(debits)

        for category in self.categorys:
            invoices = list(filter(
                lambda debit: debit.category == category, debits
            ))
            value_amount = self.calc(invoices)
            invoice_dict[category] = value_amount

        return invoice_dict
