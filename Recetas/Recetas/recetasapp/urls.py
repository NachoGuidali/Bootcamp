from django.urls import path
from .views import home, contacto, register_view, login_view, logout_view, receta_view


urlpatterns = [
    
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', register_view, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('<slug:slug>', receta_view, name="receta"),


]