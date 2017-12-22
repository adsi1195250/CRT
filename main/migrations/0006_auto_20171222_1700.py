# Generated by Django 2.0 on 2017-12-22 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_trabajadores_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codigobarras',
            name='idTrabajadores',
        ),
        migrations.RemoveField(
            model_name='trabajadores',
            name='foto',
        ),
        migrations.AddField(
            model_name='trabajadores',
            name='CodigoBarras',
            field=models.CharField(default=12, max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CodigoBarras',
        ),
    ]
