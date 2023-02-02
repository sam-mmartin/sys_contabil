import datetime
from flaskr.dto.category_reponse_dto import CategoryReponseDto
from flaskr.models.category import Category
from flaskr.sqlite import get_db


class CategoryRepository:

    def __init__(self) -> None:
        self.db = get_db()

    def list_all(self):
        categorys = self.db.execute(
            'SELECT * FROM category'
        ).fetchall()

        return self.parse(categorys)

    def list_by_description(self, description):
        category: Category = self.db.execute(
            'SELECT * FROM category WHERE description = ?',
            (description,)
        ).fetchone()

        return category

    def create(self, description):
        today = datetime.date.today()

        self.db.execute(
            'INSERT INTO category (description, date_create, date_update)'
            ' VALUES (?, ?, ?)',
            (description, today, today)
        )

        self.db.commit()

    def parse(self, categorys):
        res = []

        for item in categorys:
            category = CategoryReponseDto(
                item[0], item[1], item[2], item[3]
            )
            res.append(category)

        return res
