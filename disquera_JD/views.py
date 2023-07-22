from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.

#class BaseView(generic.ListView):
#    template_name = 'base.html'


#def base(request):
#    return render(request,'artistas/index.html')

def index (request):
    return render(request, 'artistas/index.html')

def addartista(request):
    return render(request, 'artistas/crear.html')

def editartista(request):
    return render(request, 'artistas/aditar.html' ) 

def artis(request):
    return render(request, 'seciones/artistas.html')

def songs(request):
    return render(request, 'seciones/canciones.html')

def albums(request):
    return render(request, 'albums/albums.html')

def addalbums(request):
    return render(request, 'albums/crear.html')

def editalbums(request):
    return render(request, 'albums/editar.html' ) 

def genero(request):
    return render(request, 'seciones/genero.html')