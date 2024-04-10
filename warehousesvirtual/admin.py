from django.contrib import admin
from warehousesvirtual.models import Tipo_Negocio, Unidad_Medida, Pais, Ciudad, Zonas

# Register your models here.


class Tipo_NegocioAdmin(admin.ModelAdmin):
    list_display = ["id", "descripcion"]
admin.site.register(Tipo_Negocio, Tipo_NegocioAdmin)

class Unidad_MedidaAdmin(admin.ModelAdmin):
    list_display=["id","codigo_medida","nombre_medida"]
admin.site.register(Unidad_Medida, Unidad_MedidaAdmin)


class PaisAdmin(admin.ModelAdmin):
    list_display=["id","nombre","numero_habitantes", "extension", "unidad_med"]
admin.site.register(Pais, PaisAdmin)


class CiudadAdmin(admin.ModelAdmin):
    list_display=["id","nombre","numero_habitantes", "extension", "unidad_med", "pais"]
admin.site.register(Ciudad, CiudadAdmin)

class ZonasAdmin(admin.ModelAdmin):
    list_display=["id", "zona", "ciudad", "comentarios"]
admin.site.register(Zonas, ZonasAdmin)
