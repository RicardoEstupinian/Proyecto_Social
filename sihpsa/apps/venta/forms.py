from django import forms
from apps.venta.models import Articulo


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo

        fields = [
            'categoria',
            'nombre_articulo',
            'precio',
            'estado',
            'existencia',
            'descripcion',
            'imagen_articulo',
            'vendible',
        ]

        labels = {
            'categoria': 'Categoria',
            'nombre_articulo': 'Nombre Articulo',
            'precio': 'Precio',
            'estado': 'Estado Articulo',
            'existencia': 'Existencia',
            'descripcion': 'Descripcion',
            'vendible': '¿Es Vendible?',
            'imagen_articulo': 'Imagen',
        }

        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control', 'value': 'Seleccione Categoria'}),
            'nombre_articulo': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'existencia': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'vendible': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'imagen_articulo': forms.FileInput(),
        }
