from djongo import models
from django import forms
# Create your models here.
class DetalleVentas(models.Model):
    cantidad_producto = models.IntegerField(null=True)
    codigo_producto = models.IntegerField(null=True)
    valor_total = models.FloatField(null=True)
    valor_venta = models.FloatField(null=True)
    valoriva = models.FloatField()
    objects = models.DjongoManager()
    class Meta:
        abstract = True

class DetalleVentasForm(forms.ModelForm):

    class Meta:
        model = DetalleVentas
        fields = (
            'cantidad_producto', 'codigo_producto', 'valor_total', 'valor_venta', 'valoriva'
                )

class Ventas(models.Model):
    cedula_cliente = models.IntegerField(primary_key=True, unique=False)
    codigo_venta = models.IntegerField(null=True) 
    detalle_venta = models.ArrayField(model_container=DetalleVentas, model_form_class = DetalleVentasForm, null=True)
    iva_venta = models.FloatField(null=True)
    total_venta = models.FloatField(null=True)
    valor_venta = models.FloatField(null=True)
    objects = models.DjongoManager()



