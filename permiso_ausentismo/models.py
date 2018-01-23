from datetime import date

import django
from django.db import models
from django.utils import timezone
# Create your models here.
from main.models import Trabajadores


class PermisoAusentismo(models.Model):
    idPermisoAusentismo = models.AutoField(primary_key=True)
    MESES=(
        (1,'Enero'),
        (2,'Febrero'),
        (3,'Marzo'),
        (4,'Abril'),
        (5,'Mayo'),
        (6,'Junio'),
        (7,'Julio'),
        (8,'Agosto'),
        (9,'Septiembre'),
        (10,'Octubre'),
        (11,'Noviembre'),
        (12,'Diciembre'),
    )
    mes_evento = models.SmallIntegerField(
        choices=MESES,
        default=1,
    )
    TIPO_EVENTO = (
        (1,'A.T'),
        (2, 'E.L'),
        (3, 'A.C-E.G'),
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
    codigoDiagnostico = models.CharField(max_length=4)
    observaciones = models.CharField(max_length=500,blank=True,null=True)
    idTrabajador = models.ForeignKey(Trabajadores, on_delete= models.CASCADE)
    def __str__(self):
        return '%s'%self.idPermisoAusentismo
