from django import forms
from django.forms import ModelForm
from productos.models import Producto, CategoriaProducto

class CategoriaForm(ModelForm):
    class Meta:
        model=CategoriaProducto
        fields=['nombre','descripcion']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['code','number','und_medida','tipo','categoria','nombre','descripcion', 'imagen', 'precio',
                  'afecto', 'stock', 'estado']
        exclude=['igv']
