from django.db import models
from proveedores.models import Proveedor

# Create your models here.
TAX_VALUE = 0.18
"""
class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=400)

    def __unicode__(self):
        return u'%s' % (self.nombre)
"""
tp = (
        ('01', 'Mercaderia'),
        ('02', 'Producto Terminado'),
        ('03', 'Materias Primas y Auxiliares'),
        ('04', 'Envases y Envalajes'),
        ('05', 'Suministros Diversos'),
        ('06', 'Inmueble Maquinaria y Equipo'),
    )

u = (
        ('01','KILOGRAMOS'),
        ('02','LIBRAS'),
        ('03','TONELADAS LARGAS'),
        ('04','TONELADAS METRICAS'),
        ('05','TONELADAS CORTAS'),
        ('06','GRAMOS'),
        ('07','UNIDADES'),
        ('08','LITROS'),
        ('09','GALONES'),
        ('10','BARRILES'),
        ('11','LATAS'),
        ('12','CAJAS'),
        ('13','MILLARES'),
        ('14','METROS CUBICOS'),
        ('15','METROS'),
        ('99','OTROS'),
    )
class Producto(models.Model):

    # codigo = models.IntegerField()
    code = models.CharField(max_length=5, unique=True)
    number = models.IntegerField()
    und_medida=models.CharField(max_length=2, choices=u)
    tipo=models.CharField(max_length=2, choices=tp)
    #categoria = models.ForeignKey(CategoriaProducto, null=True, blank=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=300, null=True, blank=True)
    imagen = models.ImageField(upload_to="productos",verbose_name='productos', null=True, blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    afecto = models.BooleanField(default=False)
    igv = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    estado = models.BooleanField(default=True)
    pmarca = models.CharField(max_length = 50, null=True )#Marca del producto
    pcompra = models.DecimalField(max_digits = 20, decimal_places = 2)#precio compra
    pventa = models.DecimalField(max_digits = 20, decimal_places = 2)#precio venta
    cantidad = models.PositiveIntegerField()
    #pro_compra = models.OneToOneField(Proveedor)

    # def get_serial_number(self):
    #     "Get formatted value of serial number"
    #     return "%.2d-%.3d" % (self.code, self.number)

    # def save(self):
    #     "Get last value of Code and Number from database, and increment before save"
    #     top = Producto.objects.order_by('-code','-producto')[0]
    #     self.code = top.code + 1
    #     self.number = top.number + 1
    #     super(Producto, self).save()

    def __unicode__(self):
        return u'%s-%s' % (self.code, self.nombre)

    def save(self, *args, **kwargs):

        if self.afecto==True:
            self.igv = round(float(self.precio) * TAX_VALUE, 2)
            super(Producto, self).save(*args, **kwargs)
        else:
            self.igv=0
            super(Producto, self).save(*args, **kwargs)

"""
class Producto(models.Model):
    tp = (
        ('01', 'Mercaderia'),
        ('02', 'Producto Terminado'),
        ('03', 'Materias Primas y Auxiliares'),
        ('04', 'Envases y Envalajes'),
        ('05', 'Suministros Diversos'),
        ('06', 'Inmueble Maquinaria y Equipo'),
    )

    u = (
        ('01','KILOGRAMOS'),
        ('02','LIBRAS'),
        ('03','TONELADAS LARGAS'),
        ('04','TONELADAS METRICAS'),
        ('05','TONELADAS CORTAS'),
        ('06','GRAMOS'),
        ('07','UNIDADES'),
        ('08','LITROS'),
        ('09','GALONES'),
        ('10','BARRILES'),
        ('11','LATAS'),
        ('12','CAJAS'),
        ('13','MILLARES'),
        ('14','METROS CUBICOS'),
        ('15','METROS'),
        ('99','OTROS'),
    )
    nombre = models.CharField(max_length = 100)
    cproducto = models.CharField(max_length = 30)#codigo del producto
    tproducto = models.CharField(max_length = 2, choices = tp)
    tunidad = models.CharField( max_length = 2, choices = u )#unidad de medida Sunat
    pmarca = models.CharField(max_length = 50, null=True )#Marca del producto
    pcompra = models.DecimalField(max_digits = 20, decimal_places = 2)#precio compra
    pventa = models.DecimalField(max_digits = 20, decimal_places = 2)#precio venta
    descripcion = models.TextField()#descripcion brevve del producto
    pimg = models.ImageField(upload_to = 'media' )#imagen de l producto
    cantidad = models.PositiveIntegerField()
    pcompra = models.OneToOneField(Proveedor)
    uprecio = models.DecimalField(max_digits = 20 decimal_places =2)

    def __str__(self):
        return self.nombre
"""
