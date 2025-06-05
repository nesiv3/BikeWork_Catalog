# catalogs/middleware/exception_middleware.py
from django.http import JsonResponse
from catalogs.domain.exceptions import DomainException

class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except DomainException as de:
            # Captura excepciones de dominio y retorna 400 con mensaje
            return JsonResponse({'error': str(de)}, status=400)
        except Exception as e:
            # Errores inesperados -> 500 Internal Server Error
            return JsonResponse({'error': 'Internal Server Error'}, status=500)
