from django.db import models

class ClientesManager(models.Manager):
    # Aquí puedes definir métodos personalizados para el administrador si lo deseas
    pass


class Clientes(models.Model):
    HOMBRE = 1
    MUJER = 2
    GENERO_CLIENTE = (
        (HOMBRE, 'HOMBRE'),
        (MUJER, 'MUJER'),
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    A_nacim = models.DateField(null=True)
    email = models.CharField(max_length=30)
    telefono = models.IntegerField()
    genero_cliente = models.PositiveSmallIntegerField(choices=GENERO_CLIENTE,blank=True,null=True)
   
