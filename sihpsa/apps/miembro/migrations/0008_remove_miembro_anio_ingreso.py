# Generated by Django 2.0 on 2018-11-05 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miembro', '0007_auto_20181104_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miembro',
            name='anio_ingreso',
        ),
    ]
