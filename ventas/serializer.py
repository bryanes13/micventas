from rest_framework import serializers
from .models import *

class VentasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = ['codigo_venta', 'nombre_cliente','consecutivo','nitproveedor', 'nombre_producto', 'cantidad_producto', 'precio_producto']
