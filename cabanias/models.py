from django.db import models

class CabaniasManager(models.Manager):
    # Aquí puedes definir métodos personalizados para el administrador si lo deseas
    pass


class Cabanias(models.Model):
    
    nombre = models.CharField(max_length=50)
    pax = models.CharField(max_length=50)
    costo = models.IntegerField(null=True)
   
   
