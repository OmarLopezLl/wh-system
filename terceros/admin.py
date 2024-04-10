from django.contrib import admin
from terceros.models import TiposDocIdentidad, Clientes, UserClient

# Register your models here.
class TiposDocIdentidadAdmin(admin.ModelAdmin):
    list_display = ["id", "tipo_documento"]
    list_per_page = 12
    
admin.site.register(TiposDocIdentidad, TiposDocIdentidadAdmin)  


class ClientesAdmin(admin.ModelAdmin):
    list_display = ["id", "tipo_negocio", "nombre", "tipo_identidad", "doc_identidad", "telefono", "email", "direccion", "zona"] 

    list_display_links = ["id", "nombre" ]    
    list_per_page = 12
    list_filter =["tipo_identidad"]
    search_fields = ["nombre", "doc_identidad", "telefono", "email", "direccion" ]    
    list_search = ["nombre", "doc_identidad", "telefono", "email"]

admin.site.register(Clientes, ClientesAdmin)

class UserClientAdmin(admin.ModelAdmin):
    list_display=["id", "cliente", "usuario"]
    
admin.site.register(UserClient, UserClientAdmin)







