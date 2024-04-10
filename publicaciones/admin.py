from django.contrib import admin
from publicaciones.models import Publicaciones

# Register your models here.

class PublicacionesAdmin(admin.ModelAdmin):
    list_display = ["id",  "producto", "fecha_publicacion", "valor", "comentarios", "foto_html", "cliente" ]
admin.site.register(Publicaciones, PublicacionesAdmin)
