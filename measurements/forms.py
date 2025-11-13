from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'variable',
            'codigo',
            'producto',
            'cantidad',
            'estado'
            #'dateTime',
        ]

        labels = {
            'variable' : 'Variable',
            'codigo' : 'Codigo',
            'producto' : 'Producto',
            'cantidad' : 'Cantidad',
            'estado': 'Estado'
            #'dateTime' : 'Date Time',
        }