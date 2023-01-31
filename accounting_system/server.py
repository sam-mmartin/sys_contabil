from accounting_system.record_repository import RecordRepository
from scripts.file_management import FileManagement, FileManagementWeb
from scripts.system_manager import SystemManager
from scripts.finance import Finance

filename_console = "data/novo_registro_contabil.csv"
filename = "data/web_registro_contabil.csv"
fm = FileManagement(filename_console)
fm_web = FileManagementWeb(filename)
record_repository = RecordRepository(fm_web)

# PROGRAM
fm.create_file()
table = fm.load_from_file()
finance = Finance(table)


def credit_amount() -> float:
    return finance.credit_amount()


def debit_amount() -> float:
    return finance.debit_amount()


def month_debits() -> list:
    debits = [1000.00, 2000.00, 3000.00, 4000.00, 5000.00, 6000.00,
              1000.00, 2000.00, 3000.00, 4000.00, 5000.00, 6000.00]
    return debits


def invoice_amount() -> dict:
    return finance.invoice_debits()


def create_record(description, value, category, operation, date):
    record_repository.create(description, value, category, operation, date)


def list_all_debits():
    return record_repository.list_all()
