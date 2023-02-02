from flaskr.repository.category_repository import CategoryRepository


class CategoryService:

    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    def list_all_category(self):
        return self.repository.list_all()

    def create_category(self, description):
        self.repository.create(description)
