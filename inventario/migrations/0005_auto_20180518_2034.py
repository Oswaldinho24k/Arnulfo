# Generated by Django 2.0.1 on 2018-05-18 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20180328_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemalmacen',
            name='almacen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='inventario.Almacen'),
        ),
    ]
