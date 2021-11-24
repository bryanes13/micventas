from djongo import models
from django import forms
# Create your models here.
class DetalleVentas(models.Model):
    id = models.ObjectIdField()
    cantidad_producto = models.IntegerField(null=True)
    codigo_producto = models.IntegerField(null=True)
    valor_total = models.FloatField(null=True)
    valor_venta = models.FloatField(null=True)
    valoriva = models.FloatField()

class DetalleVentasForm(forms.ModelForm):

    class Meta:
        model = DetalleVentas
        fields = (
           'id','cantidad_producto', 'codigo_producto', 'valor_total', 'valor_venta', 'valoriva'
                )

class Ventas(models.Model):
    cedula_cliente = models.IntegerField(null=True)
    codigo_venta = models.IntegerField(primary_key=True) 
    detalle_venta = models.ArrayField(model_container=DetalleVentas, model_form_class = DetalleVentasForm, null=True)
    iva_venta = models.FloatField(null=True)
    total_venta = models.FloatField(null=True)
    valor_venta = models.FloatField(null=True)
    objects = models.DjongoManager()



