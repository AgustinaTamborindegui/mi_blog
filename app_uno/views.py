from django.shortcuts import render
from app_uno.models import Post
from django.http import HttpResponse

from mi_blog.app_uno.models import Pelicula


def inicio(request):

    return render( request , "app_uno/inicio.html" )

def alta_pelicula (request):

    if request.method == "POST":

        mi_formulario = alta_pelicula( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            curso = Pelicula( nombre=datos['nombre'] , año_estreno=datos['camada'])
            curso.save()

            return render( request , "alta_pelicula.html")

    return render( request, "alta_pelicula.html")

