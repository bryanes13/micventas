from rest_framework import serializers
from .models import *

class VentasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = ['cedula_cliente', 'codigo_venta', 'detalle_venta', 'iva_venta', 'total_venta', 'valor_venta']

