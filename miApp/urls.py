from django.urls import path
from . import views

urlpatterns = [
    path('', views.main , name="home"),
    path('productos/',views.productos, name="productos")
]


