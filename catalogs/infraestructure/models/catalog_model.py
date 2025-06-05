from django.db import models

class CatalogModel(models.Model):
    identity = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def to_dict(self):
        return {
            "identity": self.identity,
            "description": self.description,
            "active": self.active
        }

    class Meta:
        db_table = 'catalog'
        managed = False  # importante si no quieres que Django intente alterarla
