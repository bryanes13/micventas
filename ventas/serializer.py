from rest_framework import serializers
from .models import *

class VentasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = ['codigo_venta', 'cedula_cliente','nitproveedor', 'nombre_producto', 'cantidad_producto']
