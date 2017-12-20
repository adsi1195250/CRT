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
        
