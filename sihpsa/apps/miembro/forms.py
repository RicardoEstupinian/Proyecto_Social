from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.miembro.models import Miembro

class CuentaForm(UserCreationForm):

	class Meta:
		model=User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels={
			'username': 'Nombre de usuario',
			'first_name': 'Nombre',
			'last_name':'Apellido',
			'email': 'Correo',
		}

class MiembroForm(forms.ModelForm):

	class Meta:
		model = Miembro
		fields = [
			'nombre_m',
			'apellido_m',
			'fecha_nac',
			'estatura',
			'num_contacto',
			'direccion',
			'hermandad',
			'cargo',
			'medalla',
			'sacramentos',
			'uniformes',
			'nombre_encargado',
			'parentesco',
			'num_encargado',
			'foto_m',
		]
		labels = {
			'nombre_m': 'Nombre del miembro',
			'apellido_m': 'Apellido del miembro',
			'fecha_nac': 'Fecha de nacimiento',
			'estatura': 'Estatura',
			'num_contacto': 'Número de contacto',
			'direccion': 'Dirección',
			'hermandad': 'Hermandad',
			'cargo': 'Cargo',
			'medalla': 'Medallas',
			'sacramentos': 'Sacramentos',
			'uniformes': 'Uniformes',
			'nombre_encargado': 'Nombre del encargado',
			'parentesco': 'Parentesco',
			'num_encargado': 'Número del encargado',
			'foto_m': 'Foto',
		}
		widgets = {
			'nombre_m': forms.TextInput(),
			'apellido_m': forms.TextInput(),
			'fecha_nac': forms.DateInput(format='%d/%m/%Y'),
			'estatura': forms.TextInput(),
			'num_contacto': forms.TextInput(),
			'direccion': forms.TextInput(),
			'hermandad': forms.Select(attrs={'class':'form-control'}),
			'cargo': forms.Select(attrs={'class':'form-control'}),
			'medalla': forms.CheckboxSelectMultiple(),
			'sacramentos': forms.CheckboxSelectMultiple(),
			'uniformes': forms.CheckboxSelectMultiple(),
			'nombre_encargado': forms.TextInput(),
			'parentesco': forms.TextInput(),
			'num_encargado': forms.TextInput(),
		}