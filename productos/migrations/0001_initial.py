# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=5)),
                ('number', models.IntegerField()),
                ('und_medida', models.CharField(max_length=2, choices=[(b'01', b'KILOGRAMOS'), (b'02', b'LIBRAS'), (b'03', b'TONELADAS LARGAS'), (b'04', b'TONELADAS METRICAS'), (b'05', b'TONELADAS CORTAS'), (b'06', b'GRAMOS'), (b'07', b'UNIDADES'), (b'08', b'LITROS'), (b'09', b'GALONES'), (b'10', b'BARRILES'), (b'11', b'LATAS'), (b'12', b'CAJAS'), (b'13', b'MILLARES'), (b'14', b'METROS CUBICOS'), (b'15', b'METROS'), (b'99', b'OTROS')])),
                ('tipo', models.CharField(max_length=2, choices=[(b'01', b'Mercaderia'), (b'02', b'Producto Terminado'), (b'03', b'Materias Primas y Auxiliares'), (b'04', b'Envases y Envalajes'), (b'05', b'Suministros Diversos'), (b'06', b'Inmueble Maquinaria y Equipo')])),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(max_length=300, null=True, blank=True)),
                ('imagen', models.ImageField(upload_to=b'productos', null=True, verbose_name=b'productos', blank=True)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('afecto', models.BooleanField(default=False)),
                ('igv', models.DecimalField(max_digits=6, decimal_places=2)),
                ('stock', models.IntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(blank=True, to='productos.CategoriaProducto', null=True)),
            ],
        ),
    ]
