from django.urls import path
from . import views

urlpatterns = [
    path('', views.main , name="home"),
    path('hola/',views.saludar, name="saludar"),
    path('adios/', views.adios, name="adios")
]


