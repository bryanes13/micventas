from django.db import models

# Create your models here.

class Ventas(models.Model):
    codigo_venta=models.IntegerField(primary_key=True)
    cedula_cliente=models.IntegerField()
    nitproveedor=models.IntegerField()
    nombre_producto=models.CharField(max_length=255)
    cantidad_producto=models.IntegerField()
