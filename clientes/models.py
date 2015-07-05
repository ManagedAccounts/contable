from django.db import models

import decimal


T_CLIENTE = (
    (0, 'Juridica'),
    (1, 'Natural'),
)

ESTADO = (
    (0, 'Activo'),
    (1, 'Inactivo'),
)
class Cliente(models.Model):
    #ruc = models.IntegerField()
    ruc_dni = models.PositiveSmallIntegerField() # RUC o DNI
    razon_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    tcliente = models.SmallIntegerField(choices = T_CLIENTE,) #Tipo de Cliente
    estado = models.SmallIntegerField(choices = ESTADO,) #  estado

    def __unicode__(self):
        return U"%s-%s" % (self.ruc_dni, self.razon_social)



"""
# Create your models here.

class Cliente(models.Model):
    T_CLIENTE = (
        (0, 'Juridica'),
        (1, 'Natural'),
    )

    ESTADO = (
        (0, 'Activo'),
        (1, 'Inactivo'),
    )

    rsocial = models.CharField(max_length = 100) #Razon Social
    tcliente = models.SmallIntegerField(choices = T_CLIENTE,) #Tipo de Cliente
    rod = models.PositiveSmallIntegerField() # RUC o DNI
    direccion = models.CharField(max_length = 100) #direccion
    toc = models.PositiveSmallIntegerField() # telefono o celular
    estado = models.SmallIntegerField(choices = ESTADO,) #  estado

    def __str__(self):
        return self.rsocial
"""

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('clientes', [int(self.pk)])
