# Generated by Django 2.0 on 2018-12-12 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0002_auto_20181212_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='directivo',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]