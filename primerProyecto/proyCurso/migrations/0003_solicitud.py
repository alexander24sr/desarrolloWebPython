# Generated by Django 4.1.4 on 2022-12-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyCurso', '0002_rename_descripion_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProductos', models.CharField(default='', max_length=512)),
                ('cantidadProductos', models.CharField(default='', max_length=512)),
            ],
        ),
    ]
