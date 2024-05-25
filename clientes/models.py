from django.db import models

class cliente (models.Model):
    id_cliente = models.IntegerField()
    nombre_cliente = models.CharField()