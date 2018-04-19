from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Page
import urllib.parse
import urllib.request


def mostrar(request):
    salida = "<ul>"
    for listado in Page.objects.all():
        salida += "<li>" + str(listado.nombre)
    salida += "</ul>"
    return HttpResponse("Contenido de la base de datos:" + salida)

@csrf_exempt
def insertar(request, texto):
    if request.method == "GET":
        try:
            p = Page.objects.get(nombre = texto)
            print()
            return HttpResponse(p.pagina)
        except Page.DoesNotExist:
            return HttpResponse("No existe una página para ese recurso.")

    else:
        p = Page(nombre = texto, pagina = request.body.decode('utf-8'))
        p.save()
        return HttpResponse("Página con el nombre: '" + str(p.nombre) + "' y el cuerpo: " + str(p.pagina) + " ha sido creada.")
