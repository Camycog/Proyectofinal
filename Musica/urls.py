from django.urls import path
from .views import signup, home

urlpatterns = [
    path('', home, name="home"),
    path('', signup, name="signup"),
]