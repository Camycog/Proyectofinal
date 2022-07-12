
from email import message
from .models import Cancion, Album, Genero 
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .serializers import CancionSerializer
from .forms import CancionForm
# Create your views here.

class CancionViewset(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

    def get_queryset(self):
        cancion = Cancion.objects.all()
        nombre = self.request.GET.get('nombre')
        if nombre:
            cancion = cancion.filter(nombre__contains="nombre")
        return cancion

def home(request):
    return render(request, 'app/home.html')

def signin(request):
    return render(request, 'app/signin.html')

def signin2(request):
    return render(request, 'app/signin2.html')

def reproductor(request):
    return render(request, 'app/reproductor.html')    


def registro(request):
    data= {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario


    return render(request, 'registration/registro.html', data)

def agregar_cancion(request):
    data= {
        'form': CancionForm()
    }
    if request.method =='POST':
        formulario=CancionForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Guardado Correctamente"
        else:
            data["form"]=formulario
    return render(request, 'app/agregar.html',data)

