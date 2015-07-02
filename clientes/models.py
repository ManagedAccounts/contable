from django.db import models

import decimal



class Cliente(models.Model):
    ruc = models.IntegerField()
    razon_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)

    def __unicode__(self):
        return U"%s-%s" % (self.ruc, self.razon_social)



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
<<<<<<< HEAD
"""
=======

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('clientes', [int(self.pk)])
>>>>>>> 41a1df05d3f13103a502d5c4aa12dc923f743df2
