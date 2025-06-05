from abc import ABC, abstractmethod
from catalogs.domain.entities.catalog import Catalog

class CatalogRepository(ABC):
    @abstractmethod
    def list_catalogs(self) -> list[Catalog]:
        """Retorna la lista de todos los catálogos."""
        pass
