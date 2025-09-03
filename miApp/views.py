from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("<h1>Página Principal! 🏠</h1>")

def saludar(request):
    return HttpResponse("<h1>Hola Mundo! 😊</h1>")

def adios(request):
    return HttpResponse("<h1>Adios Mundo! ☹️</h1>")
