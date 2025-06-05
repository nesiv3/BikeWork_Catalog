from catalogs.infraestructure.models.catalog_model import CatalogModel

class CatalogRepository:
    def __init__(self, session):
        self.session = session

    def list(self):
        return CatalogModel.objects.all()
