from flaskr.repository.register_repository import RegisterRepository


class PricingService:

   def __init__(self, repository: RegisterRepository) -> None:
      self.repository = repository

#    def list_pricings(self, month):
