from models.record import Record
from scripts.file_management import FileManagementWeb


class RecordRepository:

    def __init__(self, fm: FileManagementWeb) -> None:
        self.fm = fm

    def create(self, description, value, category, operation, date):
        index = self.fm.count()
        record = Record(index, description, value, category, operation, date)
        self.fm.file_write(record)

    def list_all(self) -> list:
        return self.fm.load_from_csv()
