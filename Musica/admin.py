from django.contrib import admin
from .models import Genero
from .models import Cancion
from .models import Artista
from .models import Album

admin.site.register(Genero)
admin.site.register(Cancion)
admin.site.register(Artista)
admin.site.register(Album)
