from django.db import models

# Create your models here.

class Ventas(models.Model):
    codigo_venta=models.IntegerField(primary_key=True)
    nombre_cliente=models.CharField(max_length=255, null=True)
    nitproveedor=models.IntegerField()
    consecutivo=models.IntegerField()
    nombre_producto=models.CharField(max_length=255)
    cantidad_producto=models.IntegerField()
    precio_producto=models.IntegerField()
