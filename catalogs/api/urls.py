from django.urls import path
from catalogs.api.views.catalog_view import CatalogListView
from catalogs.api.views.catalog_data_view import CatalogDataByCatalogView
from catalogs.api.views.initialview import home
from catalogs.api.views.health_check_view import health_check

urlpatterns = [
    path('catalogs/', CatalogListView.as_view(), name='catalog-list'),
    path('catalog-data/<str:catalog_identity>/', CatalogDataByCatalogView.as_view(), name='catalog-data'),
    path('', home , name='home'),
    path('health/', health_check, name='health-check'),  
]