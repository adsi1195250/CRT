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

class Dias_FestivosForms(forms.ModelForm):
    class Meta:
        model = dias_festivos
        fields=[
            'id',
            'festivos',
        ]
        widgets = {
            # Use localization and bootstrap 3
            'festivos': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', }),
        }
        labels={
            'festivos': 'Dias festivos',
        }
        
    """
    def clean_festivos(self):
        festivos=self.cleaned_data['festivos']
        fes = dias_festivos.objects.all()
        errors = []
        for i in fes:
            if i.festivos == festivos:
               raise ValidationError("Esta fecha ya existe")
    """
    
class trabajadoresForms(forms.ModelForm):
    class Meta:
        model = Trabajadores
        fields=[
            'id',
            'nombres',
            'cedula',
            'fechaIngreso',
            'fechaNacimiento',
            #'edad',
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
            'nombres': 'Nombre completo ',
            'cedula': 'Cedula ',
            'fechaIngreso': 'Fecha de ingreso ',
            'fechaNacimiento': 'Fecha nacimiento',
            'edad': 'Edad ',
            'administrador': ' Administrador',
            'telefono': 'Telefono ',
            'CodigoBarras':'Codigo de barras ',
            #'foto': 'Foto',

        }
        widgets = {
            'fechaIngreso': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', }),
            'fechaNacimiento': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', }),
        }

    def __init__(self, *args, **kwargs):
        super(trabajadoresForms, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_class = 'form-horizontal'

        self.helper.layout = Layout(
            Div(
                Div(Field('nombres'), css_class='col-sm-3', ),
                Div(Field('cedula'), css_class='col-sm-2', ),
                Div(Field('telefono'), css_class='col-sm-2', ),
                Div(
                    Div(Field('fechaIngreso'), css_class='', ),
                    css_class='col-sm-2'),
                Div(
                    Div(Field('fechaNacimiento'), css_class='', ),
                    css_class='col-sm-2'),
                #Div(Field('edad'), css_class='col-sm-1', ),
                # HTML('<p>Date: <input name="fechaIngreso" type="text" id="id_date"></p>'),
                css_class='row',

            ),
            Div(
                Div(Field('CodigoBarras',css_class='',rows='2',onkeypress='return event.keyCode!=13'),css_class='col-sm-10',),
                Div(Field('administrador', css_class=''), style='margin-top:38px;', css_class='col-sm-2', ),
                css_class='row'
            ),

            Div(
                FormActions(
                    Submit('save', 'Guardar', css_class='btn-default'),
                    HTML(
                        '<a type="button" class="btn btn-danger" href="{% url "listado_trabajadores" %}" >Cancelar</a>'),
                ),
                style='text-align:right;padding-right:1%;padding-top:1%'
            ),
        )


    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        return cedula

    def clean_CodigoBarras(self):
        CodigoBarras = self.cleaned_data['CodigoBarras']
        return CodigoBarras

    def clean_fechaIngreso(self):
        fechaIngreso= self.cleaned_data['fechaIngreso']
        return fechaIngreso

    def clean_fechaNacimiento(self):
        fechaNacimiento=self.cleaned_data['fechaNacimiento']
        return fechaNacimiento

    def clean(self):
        try:
            fechaIngreso=self.cleaned_data['fechaIngreso']
        except KeyError:
            raise ValidationError('Fecha de ingreso invalida!')

        try:
            fechaNacimiento=self.cleaned_data['fechaNacimiento']
        except KeyError:
            raise ValidationError('Fecha de nacimiento invalida!')

        if fechaNacimiento != None:
            if fechaNacimiento > date.today():
                raise ValidationError('La fecha de nacimiento no puede ser mayor a la fecha actual.')
        if fechaIngreso != None:
            if fechaIngreso > date.today():
                raise ValidationError('La fecha de ingreso no puede ser mayor a la fecha actual.')
        """
            for field in iter(self.fields):
            if field != 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
        """
        CodigoBarras = self.cleaned_data['CodigoBarras']
        cedula=self.cleaned_data['cedula']
        id=self.instance.id

        if Trabajadores.objects.filter(CodigoBarras__exact=CodigoBarras,pk=id).exists():
            pass
        else:
            if Trabajadores.objects.filter(CodigoBarras__exact=CodigoBarras).exists():
                raise ValidationError('El código de barras ya se encuentra registrado')

        if Trabajadores.objects.filter(cedula__exact=cedula,pk=id).exists():
            pass
        else:
            if Trabajadores.objects.filter(cedula__exact=cedula):
                raise ValidationError('La cedula ya existe')

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
                HTML('<div class="row" style="padding-left:3%;background-color: #5a47471a"> '
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


class Historial_IOForms_prueba(forms.ModelForm):
    class Meta:
        model = Historial_IO
        fields = '__all__'

        labels = {
            'accion_jornada': 'Seleccione la acción',
            'fecha': 'Fecha',
            'hora': 'Hora',
            'id_trabajadores': 'Trabajador',
        }
        disabled_widget = forms.MultipleHiddenInput(attrs={'disabled': True})

    def __init__(self, *args, **kwargs):
        super(Historial_IOForms_prueba, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                # Div(InlineRadios('accion_jornada'), style="padding-left: 50px;border-radius:50px;"),css_class='col-sm-5'),
                # Div(Field('accion_jornada'),css_class='col-md-12'),
                HTML('<div class="row" style="padding-left:3%;"> '
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
                     '</div>'), ),
            Div(

                style='text-align:center;padding-right:1%;padding-top:1%'
            ),
            #StrictButton('Guardar', css_class='btn-default',id="submit_form_reg",type="submit"),
            Field('id_trabajadores', type='hidden', readonly=True),
            Field('accion_jornada_hora', type='hidden'),
        )

    def clean_id_trabajadores(self):
        id_trabajadores = self.cleaned_data['id_trabajadores']
        # print(id_trabajadores)
        return id_trabajadores

    def clean_accion_jornada(self):
        accion_jornada = self.cleaned_data['accion_jornada']
        return accion_jornada

    def clean_accion_jornada_hora(self):
        accion_jornada_hora = self.cleaned_data['accion_jornada_hora']
        return accion_jornada_hora

    def clean(self):
        cleaned_data = super().clean()
        accion_jornada = cleaned_data.get("accion_jornada")
        id_trabajadores = cleaned_data.get("id_trabajadores")

        # Only do something if both fields are valid so far.
        # print(accion_jornada)
        # print(id_trabajadores)
        ahora = datetime.now()
        # print(ahora.date())
        datos = Historial_IO.objects.filter(fecha__exact=ahora.date(), accion_jornada__iexact=accion_jornada,
                                            id_trabajadores__nombres__exact=id_trabajadores)
        ingreso_colaborador = Historial_IO.objects.filter(fecha__exact=ahora.date(),
                                                          id_trabajadores__nombres__exact=id_trabajadores)

        entro = False
        desayuno = False
        almuerzo = False
        pausa_activa = False
        descanso = False
        for x in ingreso_colaborador:
            if x.accion_jornada == 'EN':
                entro = True
            if accion_jornada == 'DYF':
                if x.accion_jornada == 'DYI':
                    desayuno = True
            elif accion_jornada == 'ALF':
                if x.accion_jornada == 'ALI':
                    almuerzo = True
            elif accion_jornada == 'PAF':
                if x.accion_jornada == 'PAI':
                    pausa_activa = True
            elif accion_jornada == 'DCF':
                if x.accion_jornada == 'DCI':
                    descanso = True

        if accion_jornada != 'EN' and entro == False:
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


