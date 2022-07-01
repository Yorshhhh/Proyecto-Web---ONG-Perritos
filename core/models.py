from django.db import models

from django.db.models.deletion import CASCADE 

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=1000)
    Mascota = models.ForeignKey(Mascota, on_delete=CASCADE)

    def __str__(self):
        return self.nombre

