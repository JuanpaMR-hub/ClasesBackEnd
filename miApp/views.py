from django.shortcuts import render

def main(request):
    return render(request,'home.html')

def saludar(request):
    return render(request,'saludar.html')

def adios(request):
    return render(request, 'adios.html')
