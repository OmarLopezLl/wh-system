# Generated by Django 5.0.2 on 2024-03-07 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terceros', '0005_alter_userclient_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userclient',
            options={'verbose_name': 'Usuarios Cliente', 'verbose_name_plural': 'Usuarios Clientes'},
        ),
    ]