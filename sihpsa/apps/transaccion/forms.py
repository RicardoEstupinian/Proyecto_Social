from django import forms
from apps.transaccion.models import *

class PeriodoForm(forms.ModelForm):

	class Meta:
		model = PeriodoAnualDirectivo
		fields = [
			'inicio_periodo_anual',
			'final_periodo_anual',
			'nombre_periodo',
		]
		labels = {
			'inicio_periodo_anual':'Fecha de inicio:',
			'final_periodo_anual':'Fecha de finalización:',
			'nombre_periodo':'Nombre de Periodo Directivo: ',
		}
		widgets = {
			'inicio_periodo_anual': forms.DateInput(format='%d/%m/%Y'),
			'final_periodo_anual': forms.DateInput(format='%d/%m/%Y'),
			'nombre_periodo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del periodo'}),
		}
class DirectivoForm(forms.ModelForm):

	class Meta:
		model = Directivo
		fields = [
			'cargo',
		]
		labels = {
			'cargo':'Cargo directivo:',
		}
		widgets = {
			'cargo': forms.Select(attrs= {'class' : 'form-control','value':'1'}),
		}

