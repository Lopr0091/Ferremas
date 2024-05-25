from django.db import models
class categoria (models.Model):
    id_categoria = models.IntegerField()
    detalle_categoria = models.CharField()

def __str__(self):
    return self.detalle_categoria