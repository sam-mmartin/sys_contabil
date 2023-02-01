from functools import reduce
import numpy as np


class Finance:

    categorys = []

    def __init__(self, registers):
        self.debits = list(
            filter(lambda debit: debit[0] == 'Debito', registers))
        self.credits = list(
            filter(lambda credit: credit[0] == 'Credito', registers))

    def get_debits(self):
        return self.debits

    def get_credits(self):
        return self.credits

    def set_debits(self, registers):
        self.debits = list(
            filter(lambda debit: debit[0] == 'Debito', registers))

    def set_credits(self, registers):
        self.credits = list(
            filter(lambda credit: credit[0] == 'Credito', registers))

    def append_register(self, register):
        if register[0] == "Debito":
            self.debits.append(register)
        elif register[0] == "Credito":
            self.credits.append(register)

    def amount(self):
        debit = self.balance_calc(self.debits)
        credit = self.balance_calc(self.credits)
        balance = credit - debit

        print("Montante Debito: R$ {:.2f}".format(debit))
        print("Montante Credito: R$ {:.2f}".format(credit))
        print("Saldo: R$ {:.2f}".format(balance))

    def credit_amount(self) -> float:
        return self.balance_calc(self.credits)

    def debit_amount(self) -> float:
        return self.balance_calc(self.debits)

    def balance_calc(self, rows) -> float:
        values = []

        for row in rows:
            values.append(row[1])

        res = np.sum(np.asarray(values, dtype=float))
        return round(res, 2)

    def invoice_debits(self) -> dict:
        self.set_categorys(self.debits)
        invoice_set = {}

        for category in self.categorys:
            invoices = list(filter(
                lambda debit: debit[2] == category, self.debits
            ))
            value_amount = self.balance_calc(invoices)
            invoice_set[category] = value_amount

        return invoice_set

    def set_categorys(self, registers):
        self.categorys = reduce(
            lambda reg, x: reg+[x[2]] if x[2] not in reg else reg,
            registers,
            []
        )
