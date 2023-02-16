import datetime
from flaskr.dto.groupby_request_dto import GroupByRequestDto
from flaskr.sqlite import get_db


def create(group_by: GroupByRequestDto):
   today = datetime.date.today()
   db = get_db()

   db.execute(
       'INSERT INTO group_by (description, name, date_create, date_update)'
       ' VALUES (?, ?, ?, ?)',
       (group_by.description,
        group_by.name,
        today,
        today)
   )
   db.commit()


def list_all():
   db = get_db()

   groups = db.execute('SELECT * FROM group_by').fetchall()
   return groups
