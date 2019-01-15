from django import forms
from apps.transaccion.models import *
from apps.miembro.models import *

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

class cargarDeudaForm(forms.ModelForm):
    class Meta:
        model = CuentasPorCobrar

        field = [
            'miembro',
            'tipo_cc',
            'fecha_cc',
            'monto_cc',
            'concepto_cc',
        ]
        labels = {
            'miembro': 'Nombre del miembro: ',
            'tipo_cc':'Cargo o saldar de deuda: ',
            'fecha_cc': 'Fecha: ',
            'monto_cc': 'Monto: ' ,
            'concepto_cc':  'Concepto :' ,

        }

        widgets = {
			'miembro': forms.Select(attrs= {'class' : 'form-control','value':'1'}),
			'fecha_transaccion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha'}),
			'concepto_transaccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el concepto de la transacción'}),
			'tipo': forms.Select(attrs= {'class' : 'form-control','value':'1'}, choices=(('Ingreso','Ingreso'),('Egreso','Egreso'),)),
			'monto_transaccion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el monto'}),
		}