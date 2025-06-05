from django.db import transaction

class UnitOfWork:
    def __enter__(self):
        self.tx = transaction.atomic()
        self.tx.__enter__()
        self.session = None  # Django maneja esto con el ORM directamente
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tx.__exit__(exc_type, exc_val, exc_tb)
