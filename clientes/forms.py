from django import forms
from django.forms import ModelForm
from .models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['ruc_dni', 'razon_social', 'direccion', 'telefono','tcliente','estado']
