# Generated by Django 2.0.1 on 2018-03-13 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planta_alimentos', '0009_auto_20180313_1739'),
        ('vacunas', '0005_auto_20180308_2343'),
        ('ingresos', '0010_auto_20180306_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='almacenes', to='ingresos.BusinessLine')),
            ],
        ),
        migrations.CreateModel(
            name='ItemAlmacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_u', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cantidad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('unity', models.CharField(blank=True, max_length=100, null=True)),
                ('product_type', models.CharField(blank=True, max_length=100, null=True)),
                ('almacen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='inventario.Almacen')),
                ('insumo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items_almacen', to='planta_alimentos.Insumo')),
                ('vacuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items_almacen', to='vacunas.Vacuna')),
            ],
        ),
    ]
