from django import forms
from apps.venta.models import Venta


class VentasForm(forms.ModelForm):

    class Meta:
        model = Venta

        fields = [
            'articulo',
            'concepto_venta',
            'cantidad',
            'precio_venta_unitario',
            'monto_total',
            'fecha_venta',

        ]

        labels = {
            'articulo': 'Articulo',
            'concepto_venta': 'Concepto de Venta',
            'cantidad': 'Cantidad',
            'precio_venta_unitario': 'Precio de Venta',
            'monto_total': 'Monto total',
            'fecha_venta': 'Fecha de Venta',
        }

        widgets = {
            'articulo': forms.Select(attrs={'class': 'form-control', 'value': 'Seleccione articulo a vender'}),
            'concepto_venta': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese cantidad','value':'0', 'onchange':'monto()'}),
            'precio_venta_unitario': forms.TextInput(attrs={'class': 'form-control','value':'0', 'onchange':'monto()'}),
            'monto_total': forms.TextInput(attrs={'class': 'form-control','readonly':'readonly','value':'0'}),
            'fecha_venta': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),

        }
