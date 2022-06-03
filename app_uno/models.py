from django.db import models
from django.db.models.fields import (
    BooleanField, CharField, DateField, EmailField, IntegerField,
    GenericIPAddressField, URLField, DecimalField, TimeField)


class Post (models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length=2000)
    fecha = models.DateField()

class Libro (models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    año = models.DateField()

class Pelicula (models.Model):
    nombre = models.CharField(max_length=40)
    año_estreno = models.DateField(max_length=40)