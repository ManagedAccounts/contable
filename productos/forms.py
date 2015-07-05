from django import forms
from django.forms import ModelForm
from productos.models import Producto
"""
class CategoriaForm(ModelForm):
    class Meta:
        model=CategoriaProducto
        fields=['nombre','descripcion']
"""
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['code','number','und_medida','tipo','nombre','descripcion', 'imagen', 'precio',
                  'afecto', 'stock', 'estado','pmarca','pcompra','pventa','cantidad']
        exclude=['igv']
