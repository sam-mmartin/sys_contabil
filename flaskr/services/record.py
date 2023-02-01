from datetime import datetime
from ..repository.record_repository import RecordRepository
from ..models.record import Record


class RecordService:

    def __init__(self, record_repository: RecordRepository) -> None:
        self.record_repository = record_repository

    def create_record(self,
                      description: str,
                      value: float,
                      category: str,
                      operation: str,
                      date_record: str):
        description = description.capitalize()
        category = category.capitalize()
        operation = operation.capitalize()
        date = datetime.strptime(date_record, '%d-%m-%Y').date()

        record = Record(description, value, category, operation, date)
        self.record_repository.create(record)
