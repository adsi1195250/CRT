# Generated by Django 2.0.1 on 2018-02-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permiso_ausentismo', '0008_auto_20180201_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permisoausentismo',
            name='horaFinal',
            field=models.TimeField(blank=True, default='00:00:00', null=True),
        ),
        migrations.AlterField(
            model_name='permisoausentismo',
            name='horaInicial',
            field=models.TimeField(blank=True, default='00:00:00', null=True),
        ),
    ]