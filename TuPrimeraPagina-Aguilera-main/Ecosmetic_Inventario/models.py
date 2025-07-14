# inventario/models.py
from django.db import models

class JabonFrutal(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    cantidad = models.IntegerField(verbose_name="Cantidad en stock")
    
    class Meta:
        verbose_name = "Jabón Frutal"
        verbose_name_plural = "Jabones Frutales"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class JabonFloral(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    cantidad = models.IntegerField(verbose_name="Cantidad en stock")
    
    class Meta:
        verbose_name = "Jabón Floral"
        verbose_name_plural = "Jabones Florales"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class JabonPlayero(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    cantidad = models.IntegerField(verbose_name="Cantidad en stock")
    
    class Meta:
        verbose_name = "Jabón Playero"
        verbose_name_plural = "Jabones Playeros"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
