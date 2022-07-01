from asyncore import read
from dataclasses import fields
from .models import Cancion, Genero
from rest_framework import serializers

class GeneroSerializer (serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class CancionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'
