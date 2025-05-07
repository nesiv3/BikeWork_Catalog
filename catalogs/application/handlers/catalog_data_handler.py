from catalogs.application.queries.catalog_data_query import GetCatalogDataQuery
from catalogs.domain.repositories.catalog_data_repository import CatalogDataRepository

class GetCatalogDataHandler:
    def __init__(self, repository: CatalogDataRepository):
        self.repository = repository

    def handle(self, query: GetCatalogDataQuery):
        return self.repository.get_by_catalog_identity(query.catalog_identity)