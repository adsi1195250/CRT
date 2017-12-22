from crispy_forms.bootstrap import StrictButton, FormActions
from crispy_forms.layout import Layout, Div, Submit, Button
from datetimewidget.widgets import DateTimeWidget, DateWidget

from main.models import *
from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.admin.widgets import AdminDateWidget

class trabajadoresForms(forms.ModelForm):
    class Meta:
        model = Trabajadores
        fields=[
            'id',
            'nombres',
            'cedula',
            'fechaIngreso',
            'fechaNacimiento',
            'edad',
            'area',
            'telefono',
            'CodigoBarras'
            #'foto',
        ]
        widgets = {
            # Use localization and bootstrap 3
            'fechaIngreso': DateWidget(usel10n=True, bootstrap_version=3),
            'fechaNacimiento': DateWidget(usel10n=True, bootstrap_version=3)
        }

        labels = {
            'nombres': 'Nombre completo',
            'cedula': 'Cedula',
            'fechaIngreso': 'Fecha de ingreso',
            'fechaNacimiento': 'Fecha de nacimiento',
            'edad': 'Edad',
            'area': 'Area',
            'telefono': 'Telefono',
            'CodigoBarras':'Codigo de barras',
            #'foto': 'Foto',

        }

    def __init__(self, *args, **kwargs):
        super(trabajadoresForms, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_class = 'form-horizontal'

        self.helper.layout = Layout(
            'nombres',
            'cedula',
            Div(
                Div('fechaIngreso', css_class='col-md-6', ),
                Div('fechaNacimiento', css_class='col-md-6', ),
                css_class='row',
            ),
            Div(
                Div('edad', css_class='col-md-5', ),
                Div('telefono', css_class='col-md-5',),
                Div('area', css_class='col-md-2', ),
                css_class='row',
            ),
            'CodigoBarras'
            #'foto',


        )
        """    
            for field in iter(self.fields):
            if field != 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
        """


class Historial_IOForms(forms.ModelForm):
    class Meta:
        model = Historial_IO
        fields=[
            'horaEntrada',
            'horaSalida',
            'horaDesayuno',
            'horaDescanso',
            'horaPausasActivas',
            'horaAlmuerzo',
        ]
        labels = {
            'horaEntrada': 'HORA DE ENTRADA',
            'horaSalida': 'HORA DE SALIDA',
            'horaDesayuno': 'HORA DE DESAYUNO',
            'horaDescanso': 'HORA DE DESCANSO',
            'horaPausasActivas': 'HORA DE PAUSAS ACTIVAS',
            'horaAlmuerzo': 'HORA DE ALMUERZO',
        }

class PermisoAusentismoForms(forms.ModelForm):
    class Meta:
        model = PermisoAusentismo
        fields=[
            'fechaSalida',
            #'totalHoras',
            'motivo',
            'periodoIncapacidadInicial',
            'periodoIncapacidadFinal',
            'diasIncapacidad',
            'codigoDiagnostico',
            'descripcion',
            'idTrabajador',
        ]
        labels = {
            'fechaSalida': 'FECHA DE SALIDA',
            #'totalHoras': 'TOTAL DE HORAS',
            'motivo': 'MOTIVO',
            'periodoIncapacidadInicial': 'PERIODO DE INCAPACIDAD INICIAL',
            'periodoIncapacidadFinal': 'PERIODO DE INCAPACIDAD FINAL',
            'diasIncapacidad': 'DIAS DE INCAPACIDAD',
            'codigoDiagnostico': 'CODIGO DE DIAGNOSTICO',
            'descripcion': 'DESCRIPCION',
            'idTrabajador': 'ID TRABAJADOR',
        }
