# Generated by Django 5.0.2 on 2024-03-07 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terceros', '0006_alter_userclient_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='pais',
        ),
    ]
