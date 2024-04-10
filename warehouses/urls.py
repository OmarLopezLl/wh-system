"""
URL configuration for warehouses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from warehouses.views import (
	home,
	get_paises,
	get_ciudades,
	get_zonas,
	partner,
	cliente_material,
	get_clientes,
	get_clientesCiudad,
	get_clientesPais,
	get_publicaciones,
	get_import_data,
	get_publiCliente,
	updateContador,
	iniciar_sesion,
	perfil,
	cambiar_clave,
	cerrar_sesion,
	publicaciones,
	editar_pub,
	eliminar_pub,
	crear_pub,
	nosotros,
	noticias,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
	path("paises", get_paises, name="get_paises"),
	path("ciudades/<int:id>", get_ciudades, name="get_ciudades"),
	path("zonas/<int:id>", get_zonas, name="get_zonas"),
	path("partner", partner, name="partner"),
	path("cliente_material", cliente_material, name="cliente_material"),
	path("clientes/<int:id>", get_clientes, name="get_clientes"),
	path("clientesCiudad/<int:id>", get_clientesCiudad, name="get_clientesCiudad"),
	path("clientesPais/<int:id>", get_clientesPais, name="get_clientesPais"),
	path("get_publicaciones/<int:id>", get_publicaciones, name="get_publicaciones"),
	path("publiCliente/<int:id>", get_publiCliente, name="get_publiCliente"),
	path("import_data/", get_import_data, name="get_import_data"),	
	path("updateContador/<int:id>", updateContador, name="updateContador"),
	path("iniciar_sesion/", iniciar_sesion, name="iniciar_sesion"),
	path("perfil/", perfil, name="perfil"),
	path('cambiar_clave/', cambiar_clave, name='cambiar_clave'),
	path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
	path("publicaciones/", publicaciones, name="publicaciones"),
	path("editar_pub/<int:id>", editar_pub, name="editar_pub"),
	path("eliminar_pub/<int:id>", eliminar_pub, name="eliminar_pub"),
	path("crear_pub/", crear_pub, name="crear_pub"),
	path("nosotros/<int:id>", nosotros, name="nosotros"),
	path("noticias/", noticias, name="noticias"),

]
