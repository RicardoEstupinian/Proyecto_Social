from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from apps.miembro.models import Miembro, Medalla, Sacramento, Uniforme 
from apps.miembro.forms import MiembroForm, CuentaForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
# Create your views here.
import datetime
import random
def carnet(request):
	apellidos = User.objects.latest('id').last_name.split(' ')
	year = datetime.datetime.now().year
	number1 = random.randrange(10)
	number2 = random.randrange(10)
	number3 = random.randrange(10)

	ap1=apellidos[0]
	ap2=apellidos[1]
	year_str = str(year)
	number1_str = str(number1)
	number2_str = str(number2)
	number3_str = str(number3)

	carnet = ap1[0]+ap2[0]+year_str[2:4]+number1_str+number2_str+number3_str

	return HttpResponse(carnet)


def miembro_list(request, id_miembro):
	miembro = Miembro.objects.get(id=id_miembro)
	return render(request, 'miembro/miembro_list.html', {'miembro':miembro,})

def registro(request):
	form = CuentaForm()
	form2 = MiembroForm()
	if request.is_ajax():
		form = CuentaForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()

			data={
			'message':'form is saved',
			}
	if request.method=='POST':
		form2 = MiembroForm(request.POST, request.FILES or None)
		id_cuenta = User.objects.latest('id')
		apellidos = id_cuenta.last_name.split(' ')
		year = datetime.datetime.now().year
		number1 = random.randrange(10)
		number2 = random.randrange(10)
		number3 = random.randrange(10)

		ap1=apellidos[0]
		ap2=apellidos[1]
		year_str = str(year)
		number1_str = str(number1)
		number2_str = str(number2)
		number3_str = str(number3)

		carnet = ap1[0]+ap2[0]+year_str[2:4]+number1_str+number2_str+number3_str

		if form2.is_valid():
			instance2 = form2.save(commit=False)
			instance2.user = request.user
			instance2.save()
			if 'btnGuardar' in request.POST:
				miembro = Miembro.objects.latest('id')
				miembro.cuenta_id = id_cuenta.id
				miembro.carnet = carnet
				miembro.save()
			data={
			'message':'form is saved',
			}
			return redirect('base')
	context={
		'form': form,
		'form2': form2,
		}
	return render(request, 'miembro/miembro_register.html', context)

