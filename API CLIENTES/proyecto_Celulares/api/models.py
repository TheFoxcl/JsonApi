from msilib.schema import Class
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here. aqui es donde se crea la tabla de la base de datos y que columnas tendra para llenar

class Celulares(models.Model):
    identificaci├│n = models.PositiveIntegerField()
    n├║meroDeProductosVendidos=models.PositiveIntegerField()
