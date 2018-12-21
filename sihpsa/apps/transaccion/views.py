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
	cant = 0
	periodo_anual_ex = PeriodoAnualDirectivo.objects.filter(id = id).exists()
	if periodo_anual_ex:
		periodo_anual = PeriodoAnualDirectivo.objects.get(id=id)
		periodos = Periodo.objects.filter(periodo_anual = periodo_anual)
		if periodos:
			for p in periodos:
				if p.estado_periodo:
					pass
				else:
					cant += 1
	else:
		periodo_anual = ''
		periodos=''

	if request.method == 'POST':
		#Nos permitirá crear un nuevo periodo directivo
		if 'btnNuevo' in request.POST: 
			fecha_inicio = request.POST.get('fecha_inicio')
			fecha_final = request.POST.get('fecha_final')
			periodo= Periodo(
				periodo_anual = periodo_anual,
				inicio_periodo =fecha_inicio,
				final_periodo = fecha_final,
				estado_periodo = False
				)
			periodo.save()
			return redirect('periodo_list',id)
		if 'idPeriodo' in request.POST:
			periodo = Periodo.objects.get(id = request.POST.get('idPeriodo'))
			periodo.estado_periodo = True
			periodo.save()
			return redirect('periodo_list',id)

	contexto ={
	'periodo_lista' : periodos,
	'cant':cant,
	'periodo_anual':periodo_anual,
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
	directiva_completa = False
	miembros = list()
	fecha = datetime.now()
	form = DirectivoForm()
	miembros_lista = Miembro.objects.all()
	existe_directivo= Directivo.objects.filter(estado=False).exists()

	if existe_directivo:
		directivos = Directivo.objects.filter(estado=False).order_by('-id')
		if len(directivos) == 8:
			directiva_completa = True

		for m in miembros_lista:
			hay_coincidencia = False
			for d in directivos:
				if m == d.miembro:
					hay_coincidencia = True
			if hay_coincidencia:
				pass
			else:
				miembros.append(m)
	else:
		directivos = ''
		miembros=miembros_lista

	if request.method == 'POST':
		if 'btnCancelar' in request.POST:
			directivo_delete = Directivo.objects.get(id=request.POST.get('inputCancelar'))
			directivo_delete.delete()
			return redirect('asignar_directiva')
		if 'btnFinalizar' in request.POST:
			periodo_anual = PeriodoAnualDirectivo.objects.get(estado_periodo_anual=False)
			periodo_anual.directiva_asignada = True
			periodo_anual.save()
			return redirect('periodo_directivo')
		if 'btnAsignar' in request.POST:
			cargo = CargoDirectivo.objects.get(id = request.POST.get('cargo'))
			for d in directivos:
				if d.cargo == cargo:
					d.delete()

			miembro = Miembro.objects.get(id=request.POST.get('inputAsignar'))
			periodo_anual = PeriodoAnualDirectivo.objects.get(estado_periodo_anual=False)
			nuevo_directivo = Directivo(
				miembro= miembro,
				periodo = periodo_anual,
				estado = False,
				cargo = cargo
				)
			nuevo_directivo.save()
			return redirect('asignar_directiva')


	contexto ={
	'miembros':miembros,
	'fecha':fecha,
	'directivos':directivos,
	'form':form,
	'directiva_completa':directiva_completa,
	}
	return render(request, 'periodos/asignar_directiva.html',contexto)