from django.http import HttpResponse
from django.shortcuts import render
from apps.miembro.models import *
from apps.transaccion.models import *
from apps.transaccion.forms import *
from apps.miembro.models import *
from django.views.generic import View
from apps.transaccion.views import *
from apps.cuentasxcobrar.forms import *
from datetime import datetime, date, time, timedelta
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView


# Create your views here.

def cargarDeuda(request):
	fecha = datetime.now()
	#traemos a la base de datos todos lo miembros
	miembros = Miembro.objects.all()
	# creamos una instancia del formulario para rednderizarlo en el template
	formulario = cargarDeudaForm()
	#acá recibiremos lo que nos mandan del formulario
	if request.method == 'POST':
		if 'btnCargar' in request.POST:
			miembro = Miembro.objects.get(id = request.POST.get('inputCargar'))
			fecha = request.POST.get('fecha')
			monto = float(request.POST.get('monto_cc'))
			concepto = request.POST.get('concepto_cc')
			nueva_cuenta = CuentasPorCobrar(
				miembro = miembro,
				fecha_cc = fecha,
				monto_cc = monto,
				concepto_cc = concepto,
				saldo_cc = monto,
				tipo_cc = 'cargo' 
				)
			nueva_cuenta.save()
			return redirect('cuentasxcobrar:cargarDeuda')
	contexto = {
	'miembros': miembros,
	'fecha': fecha,
	'formulario':formulario
	}
	return render (request, 'cuentasxcobrar/cargar_deuda.html', contexto)


def create_cxc(miembro,fecha,concepto,tipo,monto,saldo):
	if tipo == 'Ingreso':
		saldo = saldo + monto
		# += monto
		CuentasPorCobrar.save()
	elif tipo == 'Egreso':
		saldo = saldo - monto
		#CuentasPorCobrar.saldo_cc -= monto
		CuentasPorCobrar.save()
	cxc_nueva = cxc(
		miembro = miembro,
		fecha_cc= fecha,
		concepto_cc = concepto,
		tipo_cc= tipo,
		monto_cc = monto,
		saldo_cc= saldo
		)
	cxc_nueva.save()
	return 

def lista_deudores(request):
	#traemos todos los miembros
	miembros = Miembro.objects.all()

	lista_cuenta = list() #inicializamos lista
	auxiliar = list()
	
	for m in miembros:
		tiene_cuenta = CuentasPorCobrar.objects.filter(miembro= m).exists()
		if tiene_cuenta:
			acumulador = 0
			cuentas = CuentasPorCobrar.objects.filter(miembro= m)
			for c in cuentas:
				acumulador += c.saldo_cc
			auxiliar.append(m)
			auxiliar.append(acumulador)
			lista_cuenta.append(auxiliar)
			auxiliar = []

	contexto ={
		'lista_cuenta':lista_cuenta,
		'fecha': datetime.now()
	}
	return render (request, 'cuentasxcobrar/listadeudores.html', contexto)

def saldar_deuda(request,id):
	formulario = cargarDeudaForm()
	existe_periodo = existe_periodo_actual()
	miembro_existe = Miembro.objects.filter(id=id).exists()
	
	if miembro_existe:
		miembro = Miembro.objects.get(id=id)
		cuentas_existe = CuentasPorCobrar.objects.filter(miembro=miembro).exists()
		if cuentas_existe:
			cuentas = CuentasPorCobrar.objects.filter(miembro=miembro)
	else:
		miembro = ''
		cuentas = ''
	#para abonar a la deuda
	if request.method == 'POST':
		if 'btnAbono' in request.POST:
			cuenta = CuentasPorCobrar.objects.get(id = request.POST.get('inputCuenta'))
			monto = float(request.POST.get('monto_cc'))
			if monto > 0 and existe_periodo:
				if monto < cuenta.saldo_cc:
					cuenta.saldo_cc -= monto
					cuenta.save()
				elif monto >= cuenta.saldo_cc:
					cuenta.delete()
				create_transaccion(
					Periodo.objects.get(estado_periodo= False),
					Tesoreria.objects.get(nombre_tesoreria='Hermandad'),
					cuenta.fecha_cc,
					cuenta.concepto_cc,
					'Ingreso',
					monto
					)

			return redirect('cuentasxcobrar:listaDeudores')


	contexto = {
	'miembro' :miembro,
	'cuentas' :cuentas,
	'formulario':formulario,
	'periodo':existe_periodo,
	'fecha':datetime.now()
	}
	return render (request, 'cuentasxcobrar/deuda.html', contexto)

'''
class cargarDeudaCreate(CreateView):
	model = CuentasPorCobrar
	form_class = cargarDeudaForm
	template_name = 'cuentasxcobrar/cargar_deuda.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(cargarDeudaCreate, self).get_context_data(**kwargs)
		if 'form_cargardeuda' not in context:
			context['form_cargardeuda'] = self.form_class(self.request.GET)
		return context


class cargarDeudaList(ListView):
	model = CuentasPorCobrar
	template_name = 'cuentasxcobrar/listadeudores.html'


class cargarDeudaUpdate(UpdateView):
	model = CuentasPorCobrar
	form_class = cargarDeudaForm
	template_name = 'cuentasxcobrar/cargar_deuda.html'
	success_url = '/'

'''



