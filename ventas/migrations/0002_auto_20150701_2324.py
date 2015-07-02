# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='producto',
            field=models.ForeignKey(to='productos.Producto', db_column=b'producto_id'),
        ),
        migrations.DeleteModel(
            name='CategoriaProducto',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
