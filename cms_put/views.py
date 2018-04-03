from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Page
import urllib.parse
import urllib.request

@csrf_exempt
# Create your views here.
def barra(request):

    formulario = """
    <form action="" method="POST">
        <input type="text" name="URL" value=""><br>
        <input type="submit" value="Enviar">
    </form>
    """

    lista = Page.objects.all()
    max_longitud = 0

    if request.method == "POST":
        direccion = urllib.parse.unquote(str(request.body).split('=')[1][:-1])

        if direccion[0:4] == 'www.':
            direccion = 'http://' + direccion
        elif direccion[0:4] != 'http':
            direccion = 'http://www.' + direccion

        try:
            dir_acortada = Page.objects.get(direccion=direccion)
            return HttpResponse("La página ya existe.")
        except:
            for longitud in lista:
                max_longitud +=  1
            dir_acortada = "http://127.0.0.1:8000/" + str(max_longitud+1)
            p = Page(direccion = direccion, dir_acortada = dir_acortada)
            p.save()

        return HttpResponse(p.direccion + " " + p.dir_acortada)

    salida = "<ul>"
    for listado in lista:
        salida += "<li><a href='" + str(listado.direccion) + "'>" + str(listado.direccion) +"</a>" + " -> " + "<a href='" + str(listado.dir_acortada) + "'>" + str(listado.dir_acortada) + "</a>"
    salida += "</ul>"
    return HttpResponse("Introduzca una URL:" + formulario + "Contenido de la base de datos:" + salida)

def redireccion(request, numero):
    try:
        dir_acortada = 'http://127.0.0.1:8000/' + numero
        direccion = str(Page.objects.get(dir_acortada = dir_acortada))
    except DoesNotExits:
        return HttpResponse("No Existe")

    with urllib.request.urlopen(direccion) as r:
        pagina = r.read().decode('utf-8')

    return HttpResponse(pagina)
