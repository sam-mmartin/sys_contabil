from flaskr.db import DbFile
from ..services.record import RecordService
from ..repository.record_repository import RecordRepository
from ..services.finance import FinanceService


class Server:

    def __init__(self, filename) -> None:
        self.db = DbFile(filename)
        self.rr = RecordRepository(self.db)
        self.rs = RecordService(self.rr)
        self.finance = FinanceService(self.rr)

    def get_finance(self):
        return self.finance

    def get_record_service(self):
        return self.rs
