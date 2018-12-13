from django.shortcuts import render
from django.http import HttpResponse
from apps.transaccion.models import *

# Create your views here.
def periodoDirectivo(request):
	cant = 0
	periodos = PeriodoAnualDirectivo.objects.all()
	if periodos:
		for p in periodos:
			if p.estado_periodo_anual:
				pass
			else:
				cant += 1

	contexto ={
	'periodos' : periodos,
	'cant':cant,
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

def crear_periodo(request):
	contexto ={
	'prueba' : "hola",
	}
	return render(request, 'periodos/crear_periodo.html',contexto)