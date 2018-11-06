from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def periodoDirectivo(request):
	contexto ={
	'prueba' : "hola",
	}
	return render(request, 'transaccion/periodos_directivos.html',contexto)