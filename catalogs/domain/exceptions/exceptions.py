class DomainException(Exception):
    """Excepción base de dominio."""
    pass

class CatalogNotFound(DomainException):
    """Se lanza si no se encuentra un catálogo dado."""
    pass
