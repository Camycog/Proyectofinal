from django.db import router
from django.urls import path, include
from .views import home, signin, signin2, registro, reproductor
from .views import CancionViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cancion', CancionViewset)


urlpatterns = [
    path('', home, name="home"),
    path('signin/', signin, name="signin"),
    path('signin2/', signin2, name="signin2"),
    path('reproductor/', reproductor, name="reproductor"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
]