from flaskr.db import DbFile
from ..models.record import Record


class RecordRepository:

    def __init__(self, fm: DbFile) -> None:
        self.fm = fm

    def create(self, record: Record):
        index = self.fm.count()
        index += 1
        record.set_id(index)
        self.fm.file_write(record)

    def list_all(self) -> list:
        return self.fm.load_from_csv()
