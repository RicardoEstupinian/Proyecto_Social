from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
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


def miembro_view(request, id_miembro):
	miembro = Miembro.objects.get(id=id_miembro)
	return render(request, 'miembro/miembro_view.html', {'miembro':miembro,})

def miembro_administrations(request, cargo_m='Todos'):
	activo=''
	if cargo_m == 'Crucificador':
		activo = ['actives','','','','','']
	if cargo_m == 'Jefe de disciplina':
		activo = ['','actives','','','','']
	if cargo_m == 'Custodia dolorosa':
		activo = ['','','actives','','','']
	if cargo_m == 'Ungidora':
		activo = ['','','','actives','','']
	if cargo_m == 'Jefe de grupo':
		activo = ['','','','','actives','']
	if cargo_m == 'Cargador mayor':
		activo = ['','','','','','actives']

	miembros = Miembro.objects.filter(cargo__nombre_cargo=cargo_m).order_by('apellido_m')

	if cargo_m == 'Todos':
		miembros = Miembro.objects.all().order_by('apellido_m')

	if request.method=='POST':
		if 'btnBloquear' in request.POST:
			id_user=request.POST.get('idBloquear')
			user = User.objects.get(id=id_user)
			if user.is_active:
				user.is_active=False
			else:
				user.is_active=True
			user.save()
			return redirect('miembro:administrar', cargo_m = cargo_m)

	if 'q' in request.GET:
		q=request.GET['q']
		miembros = Miembro.objects.filter(nombre_m__icontains=q).order_by('apellido_m')
		return render(request, 'miembro/miembro_administrations.html', {'miembros':miembros,'query':q})

	context = {
		'miembros': miembros,
		'cargo': cargo_m,
		'activo': activo,
	}

	return render(request, 'miembro/miembro_administrations.html', context)

def miembro_register(request):
	form = CuentaForm()
	form2 = MiembroForm()
	if request.is_ajax():
		form = CuentaForm(request.POST)
		if form.is_valid():
			form.save()

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

			data={
			'carnet': carnet,
			}
			return JsonResponse(data)
	if request.method=='POST':
		form2 = MiembroForm(request.POST, request.FILES or None)
		id_cuenta = User.objects.latest('id')

		if form2.is_valid():
			instance2 = form2.save(commit=False)
			instance2.user = request.user
			instance2.save()
			if 'btnGuardar' in request.POST:
				miembro = Miembro.objects.latest('id')
				miembro.cuenta_id = id_cuenta.id
				miembro.save()
				form2.save_m2m()
			return redirect('base')
	context={
		'form': form,
		'form2': form2,
		}
	return render(request, 'miembro/miembro_register.html', context)

def miembro_update(request, id_miembro):
	miembro = Miembro.objects.get(id=id_miembro)
	if request.method == 'GET':
		form = MiembroForm(instance=miembro)
	else:
		form = MiembroForm(request.POST, request.FILES or None, instance=miembro)
		if form.is_valid():
			form.save()
		return redirect('base')
	return render(request, 'miembro/miembro_update.html', {'form':form, 'miembro':miembro,},)

def miembro_lock(request, miembro_id):
	miembro = Miembro.objects.get(id=miembro_id)
	miembro.is_active=False
	miembro.save()
