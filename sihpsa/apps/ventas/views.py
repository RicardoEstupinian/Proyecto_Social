from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.venta.models import Articulo, Categoria
from apps.venta.forms import ArticuloForm
from apps.venta.models import Venta
from apps.ventas.forms import VentasForm
from django.shortcuts import render, redirect
from django.views.generic import ListView
from apps.transaccion.views import *

# Create your views here.
class Lista(ListView):
	model = Venta
	template_name = 'ventas/Listar.html'

'''def Listar(request):
	lista = Venta.objects.all()
	contexto = {'lista': lista}
	return render(request, 'ventas/Listar.html', contexto)'''

def Cargar(request):
	existe_periodo = existe_periodo_actual()#devuelve true si hay un periodo vigente
	error = False
	articulos = Articulo.objects.all()
	contexto = {'articulo': articulos}
	form =VentasForm()
	if request.method == 'POST':
		if existe_periodo:
			form = VentasForm(request.POST)
			if form.is_valid():
				cantida = request.POST.get('cantidad')
				nombre = request.POST.get('articulo')
				articul = Articulo.objects.get(id=nombre)
				a = articul.existencia
				b = articul.vendible
				if b == False:
					error = True
				elif int(cantida) > a:
					error = True
				else:
					a = a - int(cantida)
					articul.existencia=a
					articul.save()
					form.save()
					#se crea la transaccion con el metodo create_transaccion importado de la view de transaccion
					create_transaccion(
					Periodo.objects.get(estado_periodo= False),
					Tesoreria.objects.get(nombre_tesoreria='Hermandad'),
					request.POST.get('fecha_venta'),
					request.POST.get('concepto_venta'),
					'Ingreso',
					float(request.POST.get('monto_total'))
					)
				return redirect('ventas:Lista')
	else:
		form=VentasForm()
	return render(request,'ventas/ventas.html',{'form': form , 'error':error,'existe_periodo':existe_periodo})

