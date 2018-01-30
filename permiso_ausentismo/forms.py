from crispy_forms.bootstrap import FormActions, FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Field, HTML
from django import forms
from django.core.exceptions import ValidationError

from permiso_ausentismo.models import PermisoAusentismo


class PermisoAusentismoForms(forms.ModelForm):
    class Meta:
        model = PermisoAusentismo
        fields= '__all__'

        labels = {
            'mes_evento':'Mes ',
            'fechaSalida': 'Fecha de salida ',
            'tipo_evento':'Tipo de evento ',
            #'totalHoras': 'TOTAL DE HORAS',
            'periodoIncapacidadInicial': 'Periodo inicial',
            'periodoIncapacidadFinal': 'Periodo final',
            'totalDiasIncapacidad': 'Total de días',
            'diasCargados':'Días cargados ',
            'prorroga':'Prorroga',
            'codigoDiagnostico': 'Código de diagnostico ',
            'observaciones': 'Observaciones ',
            'idTrabajador': 'Colaborador ',
        }

        widgets = {
            'periodoIncapacidadInicial': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', }),
            'periodoIncapacidadFinal': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', }),
        }




    def __init__(self, *args, **kwargs):
        super(PermisoAusentismoForms, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                Div(Field('mes_evento'),css_class='col-md-2'),
                Div(Field('idTrabajador'),css_class='col-md-4'),
                Div(Field('tipo_evento'),css_class='col-md-3'),
                Div(FieldWithButtons('codigoDiagnostico',StrictButton('...',css_class='btn btn-info',data_toggle='modal',data_target="#myModal")), css_class='col-md-3'),
                css_class='row'
            ),
            Div(
                #Div(Field('periodoIncapacidadInicial'), css_class='col-md-3', ),
                Div(
                    Div(Field('periodoIncapacidadInicial'), css_class='', ),
                css_class='col-md-3'),
                Div(
                    Div(Field('periodoIncapacidadFinal'), css_class='', ),
                css_class='col-md-3'),
                # HTML('<p>Date: <input name="fechaIngreso" type="text" id="id_date"></p>'),
                #Div(Field('periodoIncapacidadFinal'), css_class='col-md-3', ),

                Div(Field('prorroga'), css_class='col-md-1', ),
                Div(Field('totalDiasIncapacidad'), css_class='col-md-3', ),
                Div(Field('diasCargados'), css_class='col-md-2', ),
                css_class='row',style='',
            ),
            Div(

                css_class='row',
            ),

            Field('observaciones'),

            Div(
                FormActions(
                    Submit('save', 'Guardar', css_class='btn-default'),
                    HTML('<a type="button" class="btn btn-danger" href="{% url "listado_permiso_ausentismo" %}" >Cancelar</a>'),
                ),
                style='text-align:right;padding-right:1%;padding-top:1%'
            ),
        )

    def clean_periodoIncapacidadInicial(self):
        periodoIncapacidadInicial=self.cleaned_data['periodoIncapacidadInicial']
        return periodoIncapacidadInicial

    def clean_periodoIncapacidadFinal(self):
        periodoIncapacidadFinal=self.cleaned_data['periodoIncapacidadFinal']
        return periodoIncapacidadFinal

    def clean(self):
        clean_data= super().clean()
        periodoIncapacidadInicial = clean_data.get('periodoIncapacidadInicial')
        periodoIncapacidadFinal = clean_data.get('periodoIncapacidadFinal')

        if periodoIncapacidadFinal != None and periodoIncapacidadInicial != None:
            if periodoIncapacidadFinal < periodoIncapacidadInicial:
                raise ValidationError('El periodo final no puede ser menor o igual al periodo inicial')
        elif periodoIncapacidadFinal == None and periodoIncapacidadInicial == None:
            print('entro')
            raise ValidationError('Ingrese el periodo inicial y el periodo final')
        else:
            if periodoIncapacidadInicial == None:
                raise ValidationError('Ingrese el periodo inicial')

            if periodoIncapacidadFinal == None:
                raise ValidationError('Ingrese el periodo Final')




