# Generated by Django 2.0.1 on 2019-01-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganado', '0006_auto_20190117_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='days_in_ranch',
            field=models.CharField(blank=True, default='0', max_length=100, null=True),
        ),
    ]