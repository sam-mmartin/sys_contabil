from flaskr.db import DbFile
from flaskr.repository.annual_sums_repository import AnnualSumsRepository
from flaskr.services.annual_sums_service import AnnualSumsService

from ..repository.register_repository import RegisterRepository

from flaskr.repository.category_repository import CategoryRepository
from flaskr.repository.operation_repository import OperationRepository

from flaskr.services.category_service import CategoryService
from flaskr.services.operation_service import OperationService

from flaskr.services.register_service import RegisterService


from flaskr.sqlite import get_db


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

    def get_annual_sums_service(self):
        repository = AnnualSumsRepository()
        reg_serv = self.get_register_service()
        return AnnualSumsService(repository, reg_serv)
