from catalogs.infraestructure.models.catalog_data_model import CatalogDataModel
from catalogs.domain.entities.catalog_data import CatalogData

class CatalogDataRepository:
    def get_by_catalog_identity(self, catalog_identity: str) -> list[CatalogData]:
        queryset = CatalogDataModel.objects.filter(catalog_identity=catalog_identity, active=True).order_by('order')
        return [CatalogData(**item.__dict__) for item in queryset]