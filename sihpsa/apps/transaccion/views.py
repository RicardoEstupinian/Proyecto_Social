from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def periodoDirectivo(request):
	contexto ={
	'prueba' : "hola",
	}
	return render(request, 'periodos/periodos_directivos.html',contexto)

def periodo_list(request,id):
	contexto ={
	'prueba' : "hola",
	}
	return render(request, 'periodos/periodos.html',contexto)

def periodo_seleccionado(request,id):
	contexto ={
	'prueba' : "hola",
	}
	return render(request, 'periodos/periodo_seleccionado.html',contexto)

def transaccion(request):
	contexto ={
	'prueba' : "hola",
	}
	return render(request, 'transaccion/transaccion.html',contexto)