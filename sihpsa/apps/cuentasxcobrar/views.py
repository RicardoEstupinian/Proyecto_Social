from django.http import HttpResponse
from django.shortcuts import render
from apps.miembro.models import *
from apps.transaccion.models import *
from apps.transaccion.forms import *
from apps.miembro.models import *
from django.views.generic import View
from apps.transaccion.views import *
from apps.cuentasxcobrar.forms import cargarDeudaForm
from datetime import datetime, date, time, timedelta
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView


# Create your views here.



def cargarDeuda(request):
    #fecha = datetime.now()
   # form_cargardeuda = cargarDeudaForm

    if request.method == 'POST':
		
        form_cargardeuda = cargarDeudaForm(request.POST)
        if form_cargardeuda.is_valid():
            form_cargardeuda.save()
            
            return redirect ('/' )

		
    else:
     form_cargardeuda = cargarDeudaForm()

    return render (request, 'cuentasxcobrar/cargar_deuda.html', {'form_cargardeuda':form_cargardeuda})


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



