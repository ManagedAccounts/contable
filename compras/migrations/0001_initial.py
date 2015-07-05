# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_remove_producto_pro_compra'),
        ('proveedores', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordencompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tcomprobante', models.CharField(max_length=2, choices=[(b'01', b'Factura'), (b'03', b'Boleta de Venta'), (b'07', b'Nota de Credito'), (b'08', b'Nota de Debito'), (b'60', b'Control Interno')])),
                ('ccompra', models.PositiveIntegerField()),
                ('tpago', models.CharField(max_length=1, choices=[(b'e', b'Efectivo'), (b'c', b'Credito')])),
                ('fecha', models.DateTimeField()),
                ('precio', models.DecimalField(max_digits=5, decimal_places=2)),
                ('aproucto', models.ManyToManyField(to='productos.Producto')),
                ('pcompra', models.ManyToManyField(to='proveedores.Proveedor')),
            ],
        ),
    ]
