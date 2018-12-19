from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.transaccion.models import *
from apps.transaccion.forms import *
from apps.miembro.models import *
from datetime import datetime, date, time, timedelta
import calendar
# Create your views here.
def periodoDirectivo(request):
	cant = 0
	form_periodo = PeriodoForm()
	periodos = PeriodoAnualDirectivo.objects.all().order_by('-id')
	if periodos:
		for p in periodos:
			if p.estado_periodo_anual:
				pass
			else:
				cant += 1

	if request.method == 'POST':
		#Nos permitirá crear un nuevo periodo directivo
		if 'btnNuevo' in request.POST: 
			fecha_inicio = request.POST.get('fecha_inicio')
			fecha_final = request.POST.get('fecha_final')
			nombre = request.POST.get('nombre_periodo')
			periodo= PeriodoAnualDirectivo(
				inicio_periodo_anual =fecha_inicio,
				final_periodo_anual = fecha_final,
				nombre_periodo = nombre,
				estado_periodo_anual = False,
				directiva_asignada = False
				)
			periodo.save()
			return redirect('periodo_directivo')
		if 'idPeriodo' in request.POST:
			periodo = PeriodoAnualDirectivo.objects.get(id = request.POST.get('idPeriodo'))
			periodo.estado_periodo_anual = True
			periodo.save()
			return redirect('periodo_directivo')

	contexto ={
	'periodos' : periodos,
	'cant':cant,
	'form_periodo':form_periodo,
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

def asignar_directiva(request):
	form_periodo = PeriodoForm()
	miembros = Miembro.objects.all()
	existe_directivo= Directivo.objects.filter(estado=False).exists()
	if existe_directivo:
		directivos = Directivo.objects.filter(estado=False)
	else:
		directivos = ''
	fecha = datetime.now()
	form = DirectivoForm()

	if request.method == 'POST':
		if 'btnAsignar' in request.POST:
			periodo_anual = PeriodoAnualDirectivo.objects.get(estado_periodo_anual=False)
			miembro = Miembro.objects.get(id=request.POST.get('inputAsignar'))
			nuevo_directivo = Directivo(
				miembro= miembro,
				periodo = periodo_anual,
				estado = False,
				cargo = "Presi"
				)
			
			return redirect('asignar_directiva')


	contexto ={
	'form_periodo' : form_periodo,
	'miembros':miembros,
	'fecha':fecha,
	'directivos':directivos,
	'form':form,
	}
	return render(request, 'periodos/asignar_directiva.html',contexto)