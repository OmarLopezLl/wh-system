# Generated by Django 5.0.2 on 2024-03-08 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terceros', '0007_remove_clientes_pais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='ciudad',
        ),
    ]