

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=140)),
                ('address', models.CharField(max_length=140)),
                ('rfc', models.CharField(default='', max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.", regex='^\\+?1?\\d{9,10}$')])),
                ('direct_contact', models.BooleanField(default=False)),
                ('name_contact', models.CharField(blank=True, max_length=140)),
                ('phone_contact', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.", regex='^\\+?1?\\d{9,10}$')])),
                ('comments_contact', models.CharField(blank=True, max_length=140, null=True)),
                ('credit', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=140)),
                ('rfc_comp', models.CharField(default='', max_length=20, unique=True)),
                ('email_comp', models.EmailField(max_length=254)),
                ('phone_compa', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe ingresarse en el formato: '7751234567'. Hasta 10 dígitos permitidos.", regex='^\\+?1?\\d{9,10}$')])),
                ('address', models.TextField(blank=True, null=True)),
                ('line_comp', models.ManyToManyField(related_name='companies', to='ingresos.BusinessLine')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CuentaBanco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('banco', models.CharField(blank=True, max_length=140, null=True)),
                ('clabe', models.CharField(blank=True, max_length=140, null=True, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sale_check', models.BooleanField(default=False)),
                ('no_scheck', models.CharField(blank=True, max_length=140, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('concepto', models.CharField(blank=True, max_length=140, null=True)),
                ('sale_date', models.DateTimeField(blank=True, null=True)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('unidad', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('is_sale', models.BooleanField(default=False)),
                ('business_line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='ingresos.BusinessLine')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='ingresos.Client')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incomes', to='ingresos.Company')),
                ('receivable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='ingresos.CuentaBanco')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('weigth', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('animal_ref', models.CharField(default='', max_length=100)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='ingresos.Sale')),
            ],
        ),
    ]
