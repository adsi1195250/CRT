# Generated by Django 2.0.1 on 2018-02-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permiso_ausentismo', '0007_permisoausentismo_totalhoras'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permisoausentismo',
            old_name='totalHoras',
            new_name='horaFinal',
        ),
        migrations.AddField(
            model_name='permisoausentismo',
            name='horaInicial',
            field=models.TimeField(blank=True, default='00:00:00'),
        ),
    ]
