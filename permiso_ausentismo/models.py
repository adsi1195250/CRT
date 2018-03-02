from datetime import date

import django
from django.db import models
from django.utils import timezone
# Create your models here.
from main.models import Trabajadores


class PermisoAusentismo(models.Model):
    idPermisoAusentismo = models.AutoField(primary_key=True)
    TIPO_EVENTO = (
        (1,'A.T Accidente de trabajo'),
        (2, 'E.L Enfermedad laboral'),
        (3, 'A.C-E.G Enfermedad general'),
        (5, 'O.E Otro tipo de evento'),
    )
    tipo_evento = models.SmallIntegerField(
        choices=TIPO_EVENTO,
        default=1,

    )
    periodoIncapacidadInicial = models.DateField()
    periodoIncapacidadFinal = models.DateField()
    prorroga = models.PositiveSmallIntegerField(default=0)
    totalDiasIncapacidad = models.PositiveSmallIntegerField(default=0)
    diasCargados = models.PositiveSmallIntegerField(default=0)
    horaInicial = models.TimeField(null=True,blank=True,)
    horaFinal = models.TimeField(null=True, blank=True,)
    codigoDiagnostico = models.CharField(max_length=4,null=False,blank=True)
    observaciones = models.CharField(max_length=150,blank=True,null=True,default='')
    idTrabajador = models.ForeignKey(Trabajadores, on_delete= models.CASCADE)
    def __str__(self):
        return '%s'%self.idPermisoAusentismo
