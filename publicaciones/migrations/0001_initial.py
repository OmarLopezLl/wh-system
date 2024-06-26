# Generated by Django 5.0.2 on 2024-02-14 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('terceros', '0003_userclient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=45)),
                ('fecha_publicacion', models.DateTimeField(blank=True)),
                ('precio', models.FloatField()),
                ('comentarios', models.TextField(blank=True)),
                ('foto_raw', models.FileField(upload_to='static/imagenes')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terceros.clientes')),
            ],
            options={
                'verbose_name': 'Almacen',
                'verbose_name_plural': 'Almacen',
            },
        ),
    ]
