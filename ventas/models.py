from django.db import models

# Create your models here.

class Ventas(models.Model):

    cedula_cliente=models.IntegerField(max_length=50, null=True)
    codigo_venta=models.IntegerField(max_length=50, null=True)
    ivacompra=models.IntegerField(max_length=50, null=True)
    nitproveedor=models.IntegerField(max_length=50, null=True)
    nombre_producto=models.CharField(max_length=255, null=True)
    precio_compra=models.IntegerField()
    precio_venta=models.IntegerField()