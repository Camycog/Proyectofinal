from asyncore import read
from dataclasses import fields
from .models import Artista, Cancion, Genero,Album
from rest_framework import serializers

class GeneroSerializer (serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class CancionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'
        
class ArtistaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'
        
class AlbumSerializer (serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
