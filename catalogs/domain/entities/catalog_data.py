from dataclasses import dataclass

@dataclass
class CatalogData:
    identity: str
    catalog_identity: str
    name: str
    description: str
    order: int
    active: bool