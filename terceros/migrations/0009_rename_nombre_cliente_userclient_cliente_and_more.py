# Generated by Django 5.0.2 on 2024-03-15 12:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terceros', '0008_remove_clientes_ciudad'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='userclient',
            old_name='nombre_cliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='userclient',
            old_name='nombre_user',
            new_name='usuario',
        ),
        migrations.AlterUniqueTogether(
            name='userclient',
            unique_together={('cliente', 'usuario')},
        ),
    ]
