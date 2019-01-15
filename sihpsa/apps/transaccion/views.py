from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from apps.transaccion.models import *
from apps.transaccion.forms import *
from apps.miembro.models import *
from datetime import datetime, date, time, timedelta
import calendar

from sihpsa.utileria import render_pdf

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

def transaccion(request):
	periodo_actual = ''
	periodo_anual = list()
	periodos = list()
	fecha = datetime.now()
	transacciones = list()
	form_transaccion = TransaccionForm()

	periodo_anual_ex= PeriodoAnualDirectivo.objects.filter(estado_periodo_anual=False).exists()
	if periodo_anual_ex:
		periodo_anual = PeriodoAnualDirectivo.objects.get(estado_periodo_anual=False)
		periodos_ex = Periodo.objects.filter(periodo_anual = periodo_anual,estado_periodo=True).exists()
		if periodos_ex:
			periodos = Periodo.objects.filter(periodo_anual = periodo_anual,estado_periodo=True).order_by('-id')

		periodo_actual_ex = Periodo.objects.filter(estado_periodo=False).exists()
		if periodo_actual_ex:
			periodo_actual = Periodo.objects.get(estado_periodo=False)
			tesoreria_ex = Tesoreria.objects.filter(nombre_tesoreria='Hermandad').exists()
			if tesoreria_ex:
				tesoreria = Tesoreria.objects.get(nombre_tesoreria='Hermandad')
				transacciones_ex = Transaccion.objects.filter(periodo=periodo_actual,tesoreria=tesoreria).exists()
				if transacciones_ex:
					transacciones = Transaccion.objects.filter(periodo=periodo_actual,tesoreria=tesoreria).order_by('-id')

	if request.method == 'POST':
		if 'btnRegistrar' in request.POST:
			periodo = periodo_actual
			tesoreria = Tesoreria.objects.get(id = request.POST.get('tesoreria'))
			fecha = request.POST.get('fecha_transaccion')
			concepto = request.POST.get('concepto_transaccion')
			tipo = request.POST.get('tipo')
			monto = float(request.POST.get('monto_transaccion'))
			if tesoreria.nombre_tesoreria == 'Todas':
				monto_primicia = round(monto *0.25,2)
				monto_social = round(monto*0.25,2)
				monto_hermandad = round((monto-monto_primicia-monto_social),2)
				create_transaccion(periodo,Tesoreria.objects.get(nombre_tesoreria='Primicia'),fecha,concepto,tipo,monto_primicia)
				create_transaccion(periodo,Tesoreria.objects.get(nombre_tesoreria='Fondo Social'),fecha,concepto,tipo,monto_social)
				create_transaccion(periodo,Tesoreria.objects.get(nombre_tesoreria='Hermandad'),fecha,concepto,tipo,monto_hermandad)
			elif tesoreria.nombre_tesoreria == 'Primicia':
				create_transaccion(periodo,tesoreria,fecha,concepto,tipo,monto)
			elif tesoreria.nombre_tesoreria == 'Fondo Social':
				create_transaccion(periodo,tesoreria,fecha,concepto,tipo,monto)
			elif tesoreria.nombre_tesoreria == 'Hermandad':
				create_transaccion(periodo,tesoreria,fecha,concepto,tipo,monto)
			return redirect('transaccion')
		if 'btnFactura' in request.POST:
			periodo = periodo_actual
			tesoreria = Tesoreria.objects.get(id = request.POST.get('tesoreria'))
			fecha = request.POST.get('fecha_transaccion')
			concepto = request.POST.get('concepto_transaccion')
			tipo = request.POST.get('tipo')
			monto = float(request.POST.get('monto_transaccion'))
			tipo_aux = True
			if tesoreria.nombre_tesoreria == 'Todas':
				monto_primicia = round(monto *0.25,2)
				monto_social = round(monto*0.25,2)
				monto_hermandad = round((monto-monto_primicia-monto_social),2)
				create_transaccion(periodo,Tesoreria.objects.get(nombre_tesoreria='Primicia'),fecha,concepto,tipo,monto_primicia)
				create_transaccion(periodo,Tesoreria.objects.get(nombre_tesoreria='Fondo Social'),fecha,concepto,tipo,monto_social)
				create_transaccion(periodo,Tesoreria.objects.get(nombre_tesoreria='Hermandad'),fecha,concepto,tipo,monto_hermandad)
				tipo_aux = False
			elif tesoreria.nombre_tesoreria == 'Primicia':
				create_transaccion(periodo,tesoreria,fecha,concepto,tipo,monto)
			elif tesoreria.nombre_tesoreria == 'Fondo Social':
				create_transaccion(periodo,tesoreria,fecha,concepto,tipo,monto)
			elif tesoreria.nombre_tesoreria == 'Hermandad':
				create_transaccion(periodo,tesoreria,fecha,concepto,tipo,monto)
			return redirect('factura_pdf', tipo_aux= tipo_aux)

	contexto ={
	'periodo_actual' : periodo_actual,
	'periodo_anual':periodo_anual,
	'periodos':periodos,
	'fecha':fecha,
	'transacciones':transacciones,
	'form_transaccion':form_transaccion,
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

def periodo_seleccionado(request,id):
	contexto ={
	'prueba' : "hola",
	}
	return render(request, 'periodos/periodo_seleccionado.html',contexto)

class periodo_pdf(View):
	def get(self,request,*args,**kwargs):
		id = self.kwargs['id']
		contexto = {
		"fecha_sistema": datetime.now()
		}
		pdf = render_pdf("periodos/periodo.html", contexto)
		return HttpResponse(pdf,content_type="application/pdf")

class factura_pdf(View):
	def get(self,request,*args,**kwargs):
		tipo = self.kwargs['tipo_aux']
		if tipo == 'true':
			transaccion = Transaccion.objects.all().order_by('-id')[0]
			fecha = transaccion.fecha_transaccion.strftime("%d/%m/%Y")
			concepto = transaccion.concepto_transaccion
			monto = transaccion.monto_transaccion
		elif tipo == 'False':
			transacciones = Transaccion.objects.all().order_by('-id')[:3]
			monto = 0
			for t in transacciones:
				monto += t.monto_transaccion
			transaccion = transacciones[0]
			fecha = transaccion.fecha_transaccion.strftime("%d/%m/%Y")
			concepto = transaccion.concepto_transaccion
		else:
			monto = 0
			fecha = ''
			concepto = ''
			
		contexto = {
		"tipo":tipo,
		"fecha": fecha,
		"concepto":concepto,
		"monto":monto,
		"fecha_sistema": datetime.now()
		}
		pdf = render_pdf("transaccion/factura.html", contexto)
		return HttpResponse(pdf,content_type="application/pdf")

def create_transaccion(periodo,tesoreria,fecha,concepto,tipo,monto):
	if tipo == 'Ingreso':
		saldo = tesoreria.saldo_tesoreria + monto
		tesoreria.saldo_tesoreria += monto
		tesoreria.save()
	elif tipo == 'Egreso':
		saldo = tesoreria.saldo_tesoreria - monto
		tesoreria.saldo_tesoreria -= monto
		tesoreria.save()
	transaccion_nueva = Transaccion(
		periodo= periodo,
		tesoreria=tesoreria,
		fecha_transaccion= fecha,
		concepto_transaccion = concepto,
		tipo= tipo,
		monto_transaccion = monto,
		saldo_transaccion= saldo
		)
	transaccion_nueva.save()
	return 




