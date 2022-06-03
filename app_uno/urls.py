from django.urls import path
from . import views



urlpatterns = [
    path ("", views.inicio),
    path ("alta_post/", views.alta_post),
    path ("alta_libro/", views.alta_libro),
    path ("alta_pelicula/", views.alta_pelicula),
    
]