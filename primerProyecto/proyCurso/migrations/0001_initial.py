# Generated by Django 4.1.3 on 2022-11-22 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=64)),
                ('precio', models.CharField(default='', max_length=32)),
                ('nombreImagen', models.CharField(default='', max_length=64)),
                ('descripion', models.CharField(default='', max_length=512)),
                ('estado', models.CharField(default='', max_length=64)),
                ('stock', models.CharField(default='', max_length=32)),
            ],
        ),
    ]
