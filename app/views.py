from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_maps(request):
    return render(request, 'maps.html')

def mostrar_login(request):
    return render(request, 'login.html')