# Generated by Django 2.0 on 2017-12-28 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20171228_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_io',
            name='id_trabajadores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Trabajadores'),
        ),
    ]