from flaskr.db import DbFile

from ..repository.record_repository import RecordRepository
from ..repository.register_repository import RegisterRepository

from flaskr.repository.category_repository import CategoryRepository
from flaskr.repository.operation_repository import OperationRepository

from flaskr.services.category_service import CategoryService
from flaskr.services.operation_service import OperationService

from ..services.register_service import RegisterService
from ..services.record import RecordService


from flaskr.sqlite import get_db


class Server:

    def __init__(self, filename) -> None:
        self.db = DbFile(filename)
        self.rr = RecordRepository(self.db)
        self.rs = RecordService(self.rr)
        #self.finance = FinanceService(self.rr)

    # def get_finance(self):
    #     return self.finance

    def get_record_service(self):
        return self.rs


class ServerSqlite:

    def get_register_service(self):
        op_repo = OperationRepository()
        cat_repo = CategoryRepository()
        repository = RegisterRepository()
        return RegisterService(repository, op_repo, cat_repo)

    def get_operation_service(self):
        repository = OperationRepository()
        return OperationService(repository)

    def get_category_service(self):
        repository = CategoryRepository()
        return CategoryService(repository)
