from django.urls import path
from .views import home, signin, signin2

urlpatterns = [
    path('', home, name="home"),
    path('signin/', signin, name="signin"),
    path('signin2/', signin2, name="signin2"),
]