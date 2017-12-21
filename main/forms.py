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

    def __init__(self, *args, **kwargs):
        super(trabajadoresForms, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
