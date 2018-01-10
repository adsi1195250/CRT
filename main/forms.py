from crispy_forms.bootstrap import StrictButton, FormActions, InlineRadios, InlineField
from crispy_forms.layout import Layout, Div, Submit, Button, Field, ButtonHolder, HTML
from datetimewidget.widgets import DateTimeWidget, DateWidget
from django.core.exceptions import ValidationError
from django.forms import DateInput, widgets

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
        """
        widgets = {
            'fechaIngreso': DateInput(attrs={'class': 'datepicker'}),
            #'fechaIngreso': DateInput(attrs={'class': 'datepicker'}),
            #'fechaNacimiento': DateInput(attrs={'class': 'datepicker'})
        }
        """

        """
        widgets = {
            # Use localization and bootstrap 3
            'fechaIngreso': DateWidget(usel10n=True, bootstrap_version=3),
            'fechaNacimiento': DateWidget(usel10n=True, bootstrap_version=3)
        }
        """
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
                #HTML('<p>Date: <input name="fechaIngreso" type="text" id="id_date"></p>'),
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
            'fecha': 'Fecha',
            'hora': 'Hora',
            'id_trabajadores': 'Trabajador',
        }
        disabled_widget = forms.MultipleHiddenInput(attrs={'disabled': True})



    def __init__(self, *args, **kwargs):
        super(Historial_IOForms, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                #Div(InlineRadios('accion_jornada'), style="padding-left: 50px;border-radius:50px;"),css_class='col-sm-5'),
                #Div(Field('accion_jornada'),css_class='col-md-12'),
                HTML('<div class="row" style="padding-left:5%"> '
                        '<div style="padding-left: 0px"></div>'
                        '{% for x,y in form.fields.accion_jornada.choices %}'
                            '{% if y == "Inicio Pausas Activas" or y == "Fin Pausas Activas" %}'
                                '<div class="col-sm-3" style="">'
                                '<label class="radio-inline">'
                                    '<input type="radio" name="accion_jornada" value="{{ x }}"> {{ y }}'
                                        
                                '</label>'
                            '{% else %}'
                                '{% if y == "Entrada" %}'
                                    '<div class="col-sm-2" style="">'
                                    '<label class="radio-inline">'
                                        '<input type="radio" name="accion_jornada" value="{{ x }}" checked="checked"> {{ y }}'
                            
                                        
                                    '</label>'
                                '{% elif y == Salida %}'
                                    '<div class="col-sm-2" style="">'
                                    '<label class="radio-inline">'
                                        '<input type="radio" name="accion_jornada" value="{{ x }}" checked="checked"> {{ y }}'
                                        
                                    '</label>'
                                '{% else %}'
                                    '<div class="col-sm-2" style="">'
                                    '<label class="radio-inline ">'
                                        '<input type="radio" name="accion_jornada" value="{{ x }}"> {{ y }}'
                                    '</label>'
                                '{% endif %}'
                            '{% endif %}'
                            '</div>'
                        '{% endfor %}'                    
                     '</div>'),),
            Div(
                FormActions(
                    Submit('save', 'Guardar',css_class='btn-default'),
                    HTML('<a type="button" class="btn btn-danger" href="{% url "registrarJornada" %}" >Cancelar</a>'),
                ),
                style='text-align:center;padding-right:1%;padding-top:1%'
            ),
            Field('id_trabajadores', type='hidden', readonly=True),
            Field('accion_jornada_hora',type='hidden'),
        )

    def clean_id_trabajadores(self):
        id_trabajadores=self.cleaned_data['id_trabajadores']
        #print(id_trabajadores)
        return id_trabajadores

    def clean_accion_jornada(self):
        accion_jornada=self.cleaned_data['accion_jornada']
        return accion_jornada

    def clean_accion_jornada_hora(self):
        accion_jornada_hora=self.cleaned_data['accion_jornada_hora']
        return accion_jornada_hora

    def clean(self):
        cleaned_data = super().clean()
        accion_jornada = cleaned_data.get("accion_jornada")
        id_trabajadores = cleaned_data.get("id_trabajadores")

            # Only do something if both fields are valid so far.
        #print(accion_jornada)
        #print(id_trabajadores)
        ahora = datetime.now()
        #print(ahora.date())
        datos = Historial_IO.objects.filter(fecha__exact=ahora.date(), accion_jornada__iexact=accion_jornada,id_trabajadores__nombres__exact=id_trabajadores)
        ingreso_colaborador= Historial_IO.objects.filter(fecha__exact=ahora.date(),id_trabajadores__nombres__exact=id_trabajadores)

        entro=False
        desayuno=False
        almuerzo=False
        pausa_activa=False
        descanso=False
        for x in ingreso_colaborador:
            if x.accion_jornada == 'EN':
                entro=True
            if accion_jornada == 'DYF':
                if x.accion_jornada == 'DYI':
                    desayuno = True
            elif accion_jornada == 'ALF':
                if x.accion_jornada == 'ALI':
                    almuerzo=True
            elif accion_jornada == 'PAF':
                if x.accion_jornada == 'PAI':
                    pausa_activa=True
            elif accion_jornada == 'DCF':
                if x.accion_jornada == 'DCI':
                    descanso=True

        if accion_jornada != 'EN' and entro==False:
            raise ValidationError('Ingrese su ENTRADA por favor.')
        elif accion_jornada == 'DYF' and desayuno == False:
            raise ValidationError('Ingrese su INICIO DESAYUNO por favor.')
        elif accion_jornada == 'ALF' and almuerzo == False:
            raise ValidationError('Ingrese su INICIO ALMUERZO por favor.')
        elif accion_jornada == 'PAF' and pausa_activa == False:
            raise ValidationError('Ingrese su INICIO PAUSA ACTIVA por favor.')
        elif accion_jornada == 'DCF' and descanso == False:
            raise ValidationError('Ingrese su INICIO DESCANSO por favor.')

        if datos.count() > 0:
            raise ValidationError('La acción ya se encuentra registrada en este día.')



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
