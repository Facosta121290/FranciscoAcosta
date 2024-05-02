# Generated by Django 5.0.4 on 2024-05-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pintura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lienzos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True, verbose_name='Tipo de Lienzo')),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='descripción')),
            ],
            options={
                'verbose_name': 'tipo de lienzo',
                'verbose_name_plural': 'tipo de lienzo',
            },
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True, verbose_name='Herramienta a utilizar')),
            ],
            options={
                'verbose_name': 'tipos de pinturas',
                'verbose_name_plural': 'tipos de pinturas',
            },
        ),
        migrations.CreateModel(
            name='TipoPintura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True, verbose_name='Tipo de Pintura')),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True, verbose_name='descripción')),
            ],
            options={
                'verbose_name': 'tipos de pinturas',
                'verbose_name_plural': 'tipos de pinturas',
            },
        ),
        migrations.DeleteModel(
            name='ListaCategoria',
        ),
    ]