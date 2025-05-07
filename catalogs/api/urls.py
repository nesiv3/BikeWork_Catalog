from django.urls import path
from catalogs.api.views.catalog_view import CatalogListView
from catalogs.api.views.catalog_data_view import CatalogDataByCatalogView

urlpatterns = [
    path('catalogs/', CatalogListView.as_view(), name='catalog-list'),
    path('catalog-data/<str:catalog_identity>/', CatalogDataByCatalogView.as_view(), name='catalog-data'),
]