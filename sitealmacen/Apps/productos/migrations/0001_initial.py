# Generated by Django 4.1.3 on 2022-11-10 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'tipo producto',
                'verbose_name_plural': 'tipo productos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('stockmin', models.IntegerField(verbose_name='Stock Minimo')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('tipoproducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.tipoproducto')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': ' productos',
            },
        ),
    ]
