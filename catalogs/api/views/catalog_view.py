from rest_framework.views import APIView
from rest_framework.response import Response
from catalogs.application.queries.catalogs_query import GetCatalogsQuery
from catalogs.application.handlers.catalogs_handler import CatalogQueryHandler

class CatalogListView(APIView):
    def get(self, request):
        query = GetCatalogsQuery()
        handler = CatalogQueryHandler()
        result = handler.handle(query)
        return Response(result)
