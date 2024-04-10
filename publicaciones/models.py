from django.db import models
from django.utils.html import format_html
from terceros.models import Clientes

# Create your models here.
class Publicaciones(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    producto = models.CharField(max_length=45)
    fecha_publicacion = models.DateTimeField(blank=True)
    precio = models.FloatField()
    comentarios = models.TextField(blank=True)
    foto_raw = models.FileField(upload_to="static/imagenes")    
    contador = models.IntegerField(default=0)
    class Meta:
        verbose_name = "Almacen"
        verbose_name_plural = "Almacen"

    def valor(self):
        return format_html(
            '<span style="float: right">{}</span>', "{:,}".format(self.precio)
        )

    def foto_html(self):
        return format_html('<img src="/{}" style="height: 30px">', self.foto_raw)

    def __str__(self):
        return str(self.producto)