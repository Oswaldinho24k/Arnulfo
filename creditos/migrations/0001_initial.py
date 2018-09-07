# Generated by Django 2.0.1 on 2018-08-22 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acreedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=100)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('credito', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Disposicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('tipo_credito', models.CharField(choices=[('revolvente', 'revolvente'), ('simple', 'simple')], max_length=100)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=15)),
                ('plazo', models.IntegerField()),
                ('fecha_inicio', models.DateTimeField(db_index=True)),
                ('fecha_vencimiento', models.DateTimeField(db_index=True)),
                ('tasa', models.IntegerField()),
                ('gracia', models.IntegerField()),
                ('periodo_intereses', models.CharField(choices=[('mensual', 'mensual'), ('vencimiento', 'vencimiento')], max_length=100)),
                ('periodo_capital', models.CharField(choices=[('mensual', 'mensual'), ('trimestral', 'trimestral'), ('semestral', 'semestral'), ('anual', 'anual'), ('vencimiento', 'vencimiento')], max_length=100)),
                ('acreedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disposiciones', to='creditos.Acreedor')),
            ],
        ),
    ]
