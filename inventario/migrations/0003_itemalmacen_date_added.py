# Generated by Django 2.0.1 on 2018-03-28 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_almacen_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemalmacen',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
