from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cargarDeuda (request):
    return render (request,'cuentasxcobrar/cargar_deuda.html')