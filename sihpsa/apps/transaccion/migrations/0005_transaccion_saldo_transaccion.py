# Generated by Django 2.0 on 2018-12-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0004_auto_20181218_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='saldo_transaccion',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]