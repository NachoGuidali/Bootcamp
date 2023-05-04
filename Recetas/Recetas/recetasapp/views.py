from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Receta


# Create your views here.

def home(request):
    context = {
        "recetas" : Receta.objects.all()

    }
    return render(request, "home.html", context=context)


def contacto(request):
    context = {}
    return render(request, "contacto.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #ahora verificamos si el ussuario y contraseña existe y luego entra a la url
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            #si el ususario o contraseña son incorrectos, recarga la pagina con un mensaje de error
            error_message = "Usuario o Contraseña incorrecta"
            return render(request, "registration/login.html", {'error_message' : error_message})
    return render(request, "registration/login.html", {})



def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("/")
    
    return render(request, "registration/register.html", {})

def logout_view(request):
    logout(request)
    return redirect("/")


"""def receta_view(request, slug):
    receta = Receta.objects.get(slug=slug)
    #receta = get_object_or_404(Receta, slug=receta_slug)
    contexto = {
        "receta": receta
    }
    return render(request, "receta.html", context=contexto)"""
def receta_view(request, slug):
    receta = get_object_or_404(Receta, slug=slug)
    
    return render(request, 'receta.html', {'receta': receta})    