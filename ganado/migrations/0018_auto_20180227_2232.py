# Generated by Django 2.0.1 on 2018-02-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganado', '0017_auto_20180227_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raza',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]