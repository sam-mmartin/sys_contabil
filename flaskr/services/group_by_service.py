from flaskr.dto.groupby_request_dto import GroupByRequestDto
from flaskr.models.groupby import GroupBy
from flaskr.repository import group_by_repository as repository


def create_group_by(description, name):
   group_by: GroupByRequestDto = GroupByRequestDto(description, name)
   repository.create(group_by)


def list_all_groups():
   groups = repository.list_all()
   response = mapperToEntity(groups)
   return response


def mapperToEntity(groups):
   result = []

   for item in groups:
      res = GroupBy(
          item[0],
          item[1],
          item[2],
          item[3],
          item[4]
      )
      result.append(res)

   return result
