from django.urls import *
from .import views

urlpatterns = [
    path('', views.index, name='Inicio'),
    path('canciones', views.songs, name='Songs'),
    path('artistas', views.artis, name='artis'),
    path('albums', views.albums, name='albums'),
    path('genero', views.genero, name='genero'),
    path('artista/add', views.addartista, name='artista-add'),
    path('artista/edit', views.editartista, name='editar-artis'),
    path('albums/add', views.addalbums, name='albums-add'),
    path('albums/edit', views.editalbums, name='editar-albums')
    
]