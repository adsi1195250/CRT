from main.models import *
from django import forms

class trabajadoresForms(forms.ModelForm):
    class Meta:
        models = Trabajadores
        fields=[
        'nombres',
        'cedula',
        'fechaIngreso',
        'fechaNacimiento',
        'edad',
        'cargo',
        'telefono',
        'foto',
        ]
        labels = {
        'nombres': 'NOMBRE COMPLETO',
        'cedula' : 'CEDULA',
        'fechaIngreso': 'FECHA DE INGRESO',
        'fechaNacimiento': 'FECHA DE NACIMIENTO',
        'edad': 'EDAD',
        'cargo': 'CARGO',
        'telefono': 'TELEFONO',
        'foto': 'FOTO',
        }
