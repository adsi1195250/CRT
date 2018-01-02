from crispy_forms.bootstrap import StrictButton, FormActions, InlineRadios, InlineField
from crispy_forms.layout import Layout, Div, Submit, Button, Field
from datetimewidget.widgets import DateTimeWidget, DateWidget

from main.models import *
from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime, date, time, timedelta

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
            'administrador',
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
            'administrador': 'Admin',
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
                Div('administrador', css_class='col-md-2', ),
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

"""
class Historial_IOForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Historial_IOForms, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields['id_trabajadores'].disabled = True
    class Meta:
        model = Historial_IO

        fields=[
            'horaEntrada',
            'horaSalida',
            'horaInicioDesayuno',
            'horaFinDesayuno',
            'horaInicioDescanso',
            'horaFinDescanso',
            'horaInicioPausasActivas',
            'horaFinPausasActivas',
            'horaInicioAlmuerzo',
            'horaFinAlmuerzo',
            'id_trabajadores',
        ]
        widgets = {
            # Use localization and bootstrap 3
            'horaEntrada': DateTimeWidget(bootstrap_version=4),
            'horaSalida': DateTimeWidget( bootstrap_version=3),
            'horaDescanso': DateTimeWidget(bootstrap_version=3),
            'horaDesayuno': DateTimeWidget(bootstrap_version=3),
            'horaPausasActivas': DateTimeWidget( bootstrap_version=3),
            'horaAlmuerzo': DateTimeWidget(bootstrap_version=3),
        }
        labels = {
            'horaEntrada': 'HORA DE ENTRADA',
            'horaSalida': 'HORA DE SALIDA',
            'horaInicioDesayuno': 'HORA INICIO DE DESAYUNO',
            'horaFinDesayuno': 'HORA FIN DE DESAYUNO',
            'horaInicioDescanso': 'HORA INICIO DE DESCANSO',
            'horaFinDescanso': 'HORA FIN DE DESCANSO',
            'horaInicioPausasActivas': 'HORA INICIO DE PAUSAS ACTIVAS',
            'horaFinPausasActivas': 'HORA FIN DE PAUSAS ACTIVAS',
            'horaInicioAlmuerzo': 'HORA INICIO DE ALMUERZO',
            'horaFinAlmuerzoAlmuerzo': 'HORA FIN DE ALMUERZO',
        }
"""

class Historial_IOForms(forms.ModelForm):
    class Meta:
        model = Historial_IO
        fields = '__all__'

        labels = {
            'accion_jornada':'Seleccione la acción',
            'hora': 'Hora',
            'id_trabajadores': 'Trabajador',
        }
        disabled_widget = forms.MultipleHiddenInput(attrs={'disabled': True})

    def __init__(self, *args, **kwargs):
        super(Historial_IOForms, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        #self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        #self.helper.form_class = 'form-horizontal'

        self.helper.layout = Layout(
            Div(
                Div(InlineRadios('accion_jornada'),css_class='col-sm-12', style="background: #FAFAFA; padding: 50px;"),
                #Div(Field('accion_jornada'),css_class='col-md-12'),
                css_class='row',
            ),

            Field('id_trabajadores',type='hidden',readonly=True),
        )


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
