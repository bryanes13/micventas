from rest_framework import serializers
from .models import *

class VentasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = ['cedula_cliente', 'codigo_venta', 'ivacompra', 'nitproveedor', 'nombre_producto', 'precio_compra', 'precio_venta']