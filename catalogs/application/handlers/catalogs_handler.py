from catalogs.infraestructure.repositories.catalog_repository import CatalogRepository
from catalogs.infraestructure.unit_of_work import UnitOfWork

class CatalogQueryHandler:
    def __init__(self):
        self.uow = UnitOfWork()

    def handle(self, query):
        with self.uow:
            repo = CatalogRepository(self.uow.session)
            catalogs = repo.list()
            return [catalog.to_dict() for catalog in catalogs]
