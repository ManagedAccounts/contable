from django.contrib import admin
from productos.models import Producto, CategoriaProducto
"""
class ProductoAdmin(admin.TabularInline):
    model = Producto

admin.site.register(Factura, FacturaAdmin)
"""
"""
class ProductoAdminx(admin.ModelAdmin):

    search_fields = ('code', 'nombre',)
    list_display = (
        'code', 'number', 'categoria', 'nombre', 'precio', 'igv',)
    exclude = ['igv', ]

admin.site.register(Producto, ProductoAdminx)
# Register your models here.
"""
admin.site.register(Producto)
admin.site.register(CategoriaProducto)
