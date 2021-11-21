# Generated by Django 3.2.9 on 2021-11-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('codigo_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=255, null=True)),
                ('nitproveedor', models.IntegerField()),
                ('consecutivo', models.IntegerField()),
                ('nombre_producto', models.CharField(max_length=255)),
                ('cantidad_producto', models.IntegerField()),
                ('precio_producto', models.IntegerField()),
            ],
        ),
    ]
