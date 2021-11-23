# Generated by Django 3.2.9 on 2021-11-23 13:59

from django.db import migrations
import djongo.models.fields
import ventas.models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DetalleVentas',
        ),
        migrations.AddField(
            model_name='ventas',
            name='detalle_venta',
            field=djongo.models.fields.ArrayField(model_container=ventas.models.DetalleVentas, model_form_class=ventas.models.DetalleVentasForm, null=True),
        ),
    ]
