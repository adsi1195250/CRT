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
            'cedula': 'CEDULA',
            'fechaIngreso': 'FECHA DE INGRESO',
            'fechaNacimiento': 'FECHA DE NACIMIENTO',
            'edad': 'EDAD',
            'cargo': 'CARGO',
            'telefono': 'TELEFONO',
            'foto': 'FOTO',
        }
    def __init__(self, *args, **kwargs):
        super(trabajadoresForms, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

class CodigoBarrasForms(forms.ModelForm):
    class Meta:
        models = CodigoBarras
        fields=[
            'CodigoBarras',
            'idTrabajadores',
        ]
        labels = {
            'CodigoBarras': 'CODIGO BARRAS',
            'idTrabajadores': 'ID  TRABAJADORES',
        }

class Historial_IOForms(forms.ModelForm):
    class Meta:
        models = Historial_IO
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
        models = PermisoAusentismo
        fields=[
            'fechaSalida',
            #'totalHoras',
            'motivo',
            'periodoIncapacidadInicial',
            'periodoIncapacidadFinal',
            'diasIncapacidad',
            'codigoDiagnostico',
            'descipcion',
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
