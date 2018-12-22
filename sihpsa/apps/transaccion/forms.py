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

class TransaccionForm(forms.ModelForm):

	class Meta:
		model = Transaccion
		fields = [
			'tesoreria',
			'fecha_transaccion',
			'concepto_transaccion',
			'tipo',
			'monto_transaccion',
		]
		labels = {
			'tesoreria': 'Tesorería destino/origen:',
			'fecha_transaccion':'Fecha: ',
			'concepto_transaccion':'Concepto: ',
			'tipo': 'Tipo: ',
			'monto_transaccion':'Monto: ',
		}
		widgets = {
			'tesoreria': forms.Select(attrs= {'class' : 'form-control','value':'1'}),
			'fecha_transaccion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha'}),
			'concepto_transaccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el concepto de la transacción'}),
			'tipo': forms.Select(attrs= {'class' : 'form-control','value':'1'}, choices=(('Ingreso','Ingreso'),('Egreso','Egreso'),)),
			'monto_transaccion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el monto'}),
		}