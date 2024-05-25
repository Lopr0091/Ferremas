from django.db import models
from categoria.models import categoria
class Producto(models.Model):
    id_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=100)
    descripcion_producto = models.TextField()
    precio_producto = models.IntegerField()
    stock_producto = models.IntegerField()
    