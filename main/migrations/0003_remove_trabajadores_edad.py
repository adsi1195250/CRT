# Generated by Django 2.0.1 on 2018-01-25 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180111_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajadores',
            name='edad',
        ),
    ]