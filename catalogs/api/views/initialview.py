# filepath: c:\Documentos\Proyectos\BikeWork\BikeWork_Catalog\catalogs\views.py
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')