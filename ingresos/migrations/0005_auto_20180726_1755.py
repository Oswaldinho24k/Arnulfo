# Generated by Django 2.0.1 on 2018-07-26 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0004_sale_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['-created']},
        ),
    ]
