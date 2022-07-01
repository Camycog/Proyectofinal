from datetime import datetime
from time import time
from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete = models.DO_NOTHING)
    artista = models.CharField(max_length=100)
    duracion = models.DecimalField(max_digits=20, decimal_places=2,blank=True)

    def __str__(self):
        return self.nombre

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_artistico = models.CharField(max_length=100, )
    def __str__(self):
        return self.nombre_artistico
    
class Album(models.Model):
    nombre_album = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre_album 