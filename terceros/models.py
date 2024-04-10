from django.db import models
from django.contrib.auth.models import User
from warehousesvirtual.models import Ciudad, Tipo_Negocio, Zonas

# Create your models here.
class TiposDocIdentidad(models.Model):
    """docstring for TiposDocIdentidad"""
    tipo_documento = models.CharField(max_length=45)
    class Meta:
        verbose_name = "Tipo Doc Identidad"
        verbose_name_plural = "Tipos Doc Identidad"
    def __str__(self):
        return self.tipo_documento
    

class Clientes(models.Model):
    tipo_negocio = models.ForeignKey(Tipo_Negocio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    tipo_identidad = models.ForeignKey(TiposDocIdentidad, on_delete=models.CASCADE)
    doc_identidad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    direccion = models.CharField(max_length=100)
    zona =  models.ForeignKey(Zonas, on_delete=models.CASCADE)
    comentarios = models.TextField(blank=True)
    logo_raw = models.FileField(upload_to="static/imagenes")
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '{}'.format(self.nombre)    

class UserClient(models.Model):
    cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE )
    usuario=models.ForeignKey(User, on_delete=models.CASCADE )
    class Meta:
        verbose_name = "Usuarios Cliente"
        verbose_name_plural = "Usuarios Clientes"
        unique_together = [["cliente", "usuario"]]

    def __str__(self):
        return '{} {}'.format(self.cliente, self.usuario )   