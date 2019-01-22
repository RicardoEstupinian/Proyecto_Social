from django.shortcuts import render
from django.http import HttpResponse
from apps.venta.models import Articulo, Categoria
from apps.venta.forms import ArticuloForm
from apps.venta.models import Venta
from apps.ventas.forms import VentasForm
from django.shortcuts import render, redirect
from django.views.generic import ListView

# Create your views here.
class Lista(ListView):
	model = Venta
	template_name = 'ventas/Listar.html'

'''def Listar(request):
	lista = Venta.objects.all()
	contexto = {'lista': lista}
	return render(request, 'ventas/Listar.html', contexto)'''

def Cargar(request):
	error = False
	articulos = Articulo.objects.all()
	contexto = {'articulo': articulos}
	form =VentasForm()
	if request.method == 'POST':
		form = VentasForm(request.POST)
		if form.is_valid():
			cantida = request.POST.get('cantidad')
			nombre = request.POST.get('articulo')
			articul = Articulo.objects.get(id=nombre)
			a = articul.existencia
			b = articul.vendible
			if b == False:
				error = True
			if int(cantida) > a:
				error = True
			else:
				a = a - int(cantida)
				articul.existencia=a
				articul.save()
				form.save()
	else:
		form=VentasForm()
	return render(request,'ventas/ventas.html',{'form': form , 'error':error,})

