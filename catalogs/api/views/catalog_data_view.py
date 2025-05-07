from rest_framework.views import APIView
from rest_framework.response import Response
from catalogs.application.queries.catalog_data_query import GetCatalogDataQuery
from catalogs.application.handlers.catalog_data_handler import GetCatalogDataHandler
from catalogs.infraestructure.repositories.catalog_data_repository import CatalogDataRepository

class CatalogDataByCatalogView(APIView):
    def get(self, request, catalog_identity):
        query = GetCatalogDataQuery(catalog_identity=catalog_identity)
        handler = GetCatalogDataHandler(CatalogDataRepository())
        result = handler.handle(query)
        return Response([vars(item) for item in result])