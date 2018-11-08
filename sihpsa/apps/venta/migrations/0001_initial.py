# Generated by Django 2.0 on 2018-11-07 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_articulo', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('estado', models.CharField(max_length=100)),
                ('existencia', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen_articulo', models.ImageField(blank=True, upload_to='static/img')),
                ('vendible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto_venta', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('precio_venta_unitario', models.FloatField()),
                ('monto_total', models.FloatField()),
                ('fecha_venta', models.DateField()),
                ('articulo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='venta.Articulo')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='venta.Categoria'),
        ),
    ]
