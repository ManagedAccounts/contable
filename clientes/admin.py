from django.contrib import admin
from .models import Cliente

# Register your models here.i
class ClienteAdmin(admin.ModelAdmin):

    search_fields = ('razon_social', 'ruc',)
    list_display = (
        'razon_social', 'ruc', 'direccion', 'telefono',)

admin.site.register(Cliente, ClienteAdmin)

