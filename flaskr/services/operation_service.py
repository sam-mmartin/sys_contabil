from flaskr.repository.operation_repository import OperationRepository


class OperationService:

    def __init__(self, repository: OperationRepository) -> None:
        self.repository = repository

    def list_all_operations(self):
        return self.repository.list_all()

    def create_operation(self, description):
        self.repository.create(description)
