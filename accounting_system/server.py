from scripts.file_management import FileManagement
from scripts.system_manager import SystemManager
from scripts.finance import Finance

filename = "data/registro_contabil.csv"
sys_manager = SystemManager()
fm = FileManagement(filename)

# PROGRAM
fm.create_file()
table = fm.load_from_file()
finance = Finance(table)


def credit_amount():
    return '{:.2f}'.format(finance.credit_amount())


def debit_amount():
    return '{:.2f}'.format(finance.debit_amount())


def month_debits():
    debits = [1000.00, 2000.00, 3000.00, 4000.00, 5000.00, 6000.00,
              1000.00, 2000.00, 3000.00, 4000.00, 5000.00, 6000.00]
    return debits


def invoice_amount():
    return '{:.2f}'.format(finance.invoice_debits())
