from django.db import models

class CatalogDataModel(models.Model):
    identity = models.CharField(primary_key=True, max_length=100)
    catalog_identity = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'catalog_data'