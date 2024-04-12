# import traceback
import os
import traceback
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
import pytz 
from warehousesvirtual.models import Pais, Ciudad,Zonas
from terceros.models import Clientes, UserClient
from publicaciones.models import Publicaciones
from django.db.models import Q
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError
from datetime import datetime
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from warehousesvirtual.forms import PublicForm
from django import forms
from warehousesvirtual.resources import PersonaResource
from tablib import Dataset


# class UploadFileForm(forms.ModelForm):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

#     class Meta:
#         model = Publicaciones.foto_raw

def handle_uploaded_file(f):
    with open("static/imagenes", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def home(request):
    return render(request, "warehouses/indice.html")

def get_paises(request):
    paises = list(Pais.objects.values())
    if len(paises) > 0:
        data = {"message": "Success", "paises": paises}
        return JsonResponse(data)
    else:
        data = {"message": "not found"}
        return JsonResponse(data)
    
def get_ciudades(request, id):
    ciudades = list(Ciudad.objects.filter(pais_id=id).values())
    if len(ciudades) > 0:
        data = {"message": "Success", "ciudades": ciudades}
        return JsonResponse(data)
    else:
        data = {"message": "not found"}
        return JsonResponse(data)
    
def get_zonas(request, id):
    zonas = list(Zonas.objects.filter(ciudad_id=id).values())
    if len(zonas) > 0:
        data={"message": "Success", "zonas": zonas}
        return JsonResponse(data)
    else:
        data={"message": "not found"}
        return JsonResponse(data)
    
def partner(request):
    clientes = Clientes.objects.all().select_related("zona").values()
    contexto = {"clien": clientes}
    return render(request, "warehouses/socios.html", contexto)

@csrf_protect
def cliente_material(request):
    # mat = request.POST.get("buscar")     
    mat = request.POST["buscar"]
    pais = request.POST["pais"]
    ciudad = request.POST["ciudad"]
    zona = request.POST["zona"]
    print(mat)
    try:          
        if mat:
            if ciudad=='':
                print("busca por pais")
                print (pais)
                mater =Publicaciones.objects.filter(producto__icontains=mat, cliente__zona__ciudad__pais__id=pais).order_by('producto')
                print (mater)
            elif zona=='':
                print("busca por ciudad")
                print (ciudad)
                mater =Publicaciones.objects.filter(producto__icontains=mat, cliente__zona__ciudad__id=ciudad).order_by('producto')   
            else:
                print("busca por zona")  
                print(zona)
                mater =Publicaciones.objects.filter(producto__icontains=mat, cliente__zona__id=zona).order_by('producto')
                print (mater.all)
            context = {"mater": mater}
        else:
            mater = list(Publicaciones.objects.select_related("cliente")).order_by('producto')            
            context = {"mater": mater}
            print("cuarto paso")     
        return render(request, "publicaciones/cliente_material.html", context)
    except:
        print("error")
        mater = Publicaciones.objects.all()
        context = {"mater": ''}
        return render(request, "publicaciones/cliente_material.html", context)
       
####
## Consulta clientes     
"""
def get_clientes(request, id):
    clientes = list(Clientes.objects.filter(zona_id=id).select_related("zona"))
    # clientes = list(Clientes.objects.filter(zona_id=id).select_related("zona").values())
    if len(clientes) > 0:
        data = {"message": "Success", "clientes": clientes}
    else:
        data = {"message": "not found"}
    return JsonResponse(data)
"""
def get_clientes(request, id):
    #clientes = list(Clientes.objects.filter(zona_id=id).select_related("zona").values())
    clientes_raw = Clientes.objects.filter(zona_id=id).select_related("zona")
    if len(clientes_raw) > 0:
        mov_clie = []
        for x in clientes_raw:
            mov_clie.append({"id": x.id, "nombre": x.nombre, "direccion": x.direccion,"telefono": x.telefono, "email": x.email, "logo_raw": x.logo_raw.url, "pais": x.zona.ciudad.pais.nombre, "ciudad": x.zona.ciudad.nombre, "zona": x.zona.zona, "zona_id": x.zona_id})
        data = {"message": "Success", "clientes": mov_clie}
    else:
        data = {"message": "not found"}
    return JsonResponse(data)


def get_clientesCiudad(request, id):
    #clientes = list(Clientes.objects.filter(zona_id=id).select_related("zona").values())
    print("ID Ciudad:{}".format(id))
    # clientes_raw = Clientes.objects.filter(zona__ciudad_id=id).select_related("zona")
    clientes_raw = Clientes.objects.filter(zona__ciudad__id=id).select_related("zona") 
    if len(clientes_raw) > 0:
        mov_clie = []
        for x in clientes_raw:
            mov_clie.append({"id": x.id, "nombre": x.nombre, "direccion": x.direccion,"telefono": x.telefono, "email": x.email, "logo_raw": x.logo_raw.url, "pais": x.zona.ciudad.pais.nombre, "ciudad": x.zona.ciudad.nombre, "zona": x.zona.zona, "zona_id": x.zona_id})
           
        data = {"message": "Success", "clientesCiudad": mov_clie}
    else:
        print ("no encontrada clienteCiudad")
        mov_clie = []        
        data = {"message": "not found", "clientesCiudad": mov_clie }
    return JsonResponse(data)


def get_clientesPais(request, id):
    print("ID Pais:{}".format(id))
    # clientes_raw = Clientes.objects.filter(zona__ciudad_id=id).select_related("zona")
    clientes_raw = Clientes.objects.filter(zona__ciudad__pais__id=id).select_related("zona") 
    if len(clientes_raw) > 0:
        mov_clie = []
        for x in clientes_raw:
            mov_clie.append({"id": x.id, "nombre": x.nombre, "direccion": x.direccion,"telefono": x.telefono, "email": x.email, "logo_raw": x.logo_raw.url, "pais": x.zona.ciudad.pais.nombre, "ciudad": x.zona.ciudad.nombre, "zona": x.zona.zona, "zona_id": x.zona_id})
           
        data = {"message": "Success", "clientesPais": mov_clie}
    else:
        data = {"message": "not found" }
    return JsonResponse(data)

   
def get_publicaciones(_request, id):
    publicaciones = list(Publicaciones.objects.filter(cliente_id=id).values())
    if len(publicaciones) > 0:
        data = {"message": "Success", "publicaciones": publicaciones}
        return JsonResponse(data)
    else:
        data = {"message": "not found"}
        return JsonResponse(data)
    

# def get_import_data(request,):     
#      contexto = {"user": "userclient"}   
#      return render(request, "publicaciones/import_data.html", contexto)

# https://es.linkedin.com/pulse/importar-datos-desde-excel-en-django-python-daniel-bojorge
def get_import_data(request,):
    if request.method == 'POST':  
        persona_resource = PersonaResource()  
        dataset = Dataset()  
        print(dataset)  
        nuevas_personas = request.FILES['my_file']  
        print(nuevas_personas)  
        imported_data = dataset.load(nuevas_personas.read())  
        print(dataset)  
        result = persona_resource.import_data(dataset, dry_run=True) # Test the data import 
        #print(result.has_errors())  if not result.has_errors()  
        persona_resource.import_data(dataset, dry_run=False) # Actually import now  return render(request, 'export/importar.html')  
        contexto = {"user1": "cargado"}   
        return render(request, "publicaciones/import_data.html", contexto)
    else:
        contexto = {"user1": "userclient"}   
        return render(request, "publicaciones/import_data.html", contexto)


def get_publiCliente(request, id):
    try:
        material = Publicaciones.objects.filter(cliente_id=id)
        cliente = Clientes.objects.filter(id=id)
        cant_material = material.count()
        contexto = {
            "mater": material,
            "canti": cant_material,
            "nomc": cliente,
        }
        return render(request, "publicaciones/materiales.html", contexto)
    except:
        mensaje = "No hay datos"
        contexto = {"Errorr": mensaje}
        return render(request, "publicaciones/cliente_material.html", contexto)
    
@csrf_protect    
def updateContador(request, id):
    try:
        p = Publicaciones.objects.get(pk=id)
        p.contador = p.contador + 1
        p.save()
        mensaje = "Se actualizo el material"
        contexto = {"Successful": mensaje}
        contexto = {
        "mater": mensaje,
        "canti": p.contador,
        "nomc":  p.producto,
        }
        print(mensaje)
        print(p.contador)
        print(p.producto)
    except:
        mensaje = "No actualizo material"
        contexto = {"Errorr": contexto }
    # return render(request, "publicaciones/cliente_material.html", contexto)


    return HttpResponse(contexto)

    #return HttpResponse("No usuario registrado")

    # material = Publicaciones.objects.filter(id=id)
    # public = None  
    # if len(material) > 0:
    #     public = Publicaciones.objects.get(pk=request.Publicaciones.id)
    #     public.contador = request.POST[1]
    #     public.save()
    
   
# def get_materiales(request):
#     q = request.POST.get('material')
#     print(q)
#     if q:
#         vector = SearchVector('producto')
#         query = SearchQuery('q')
#         # material = Publicaciones.objects.filter(producto__search=q)
#         # material = Publicaciones.objects.annotate(Search= vector).filter(Search=query)
#         material = Publicaciones.objects.annotate(rank= SearchRank(vector, query)).order_by('-Rank')
#     else:
#            material = None
#     context = {"material": material}
#     return render(request, "publicaciones/materiales.html", context)
# try:
#     material = Publicaciones.objects.all()
#     return render(request, "publicaciones/materiales.html", {"mater": material })
# except:
#     material = ""
#     return render(request, "publicaciones/materiales.html", {"mater": material})
#     if mat:
#         material = Publicaciones.objects.filter(
#             Q(producto__icontains=mat)
#         ).distinct()
#     return render(request, "publicaciones/materiales.html", {"mater": material, clientes: clientes })
# except:
#     mat = ""
#     return render(request, "publicaciones/materiales.html", {"mater": material})

### Vistas de  administración de usuario    


# def get_carrito(request):
# 	if request.user.is_anonymous:
# 		usuario_sesion = 3 # Usuario anónimo
# 	else:
# 		usuario_sesion = request.user.id # Usuario autenticado
	
# 	if request.session.session_key:
# 		id_session_new = request.session.session_key
# 	else:
# 		request.session = SessionStore()
# 		request.session['Carrito_shop'] = datetime.datetime.now().timestamp()
# 		request.session.create()
# 		id_session_new = request.session.session_key

# 	items_cart = Carrito.objects.filter(usuario_id=usuario_sesion,session_id=id_session_new).count()
# 	return items_cart

def noticias(request):
    contexto = {"mater": "prueba"}
    return render(request, "warehouses/noticias.html", contexto)


@csrf_protect
def iniciar_sesion(request):
    # items_cart = get_carrito(request)
    if request.method == "POST":
        if "cuenta" in request.POST and "clave" in request.POST:
            # return HttpResponse("Cuenta:"+request.POST["cuenta"]+" Clave: "+request.POST["clave"], request)
            try:
                usuario = auth.authenticate(
                    username=request.POST["cuenta"], password=request.POST["clave"]
                )
                if usuario is not None:
                    # A backend authenticated the credentials
                    auth.login(request, usuario)
                    return HttpResponseRedirect("/", request)
                else:
                    # No backend authenticated the credentials
                    contexto = {
                        "mensaje": "Error en credenciales de Acceso!",
                        "items_cart": "",
                    }
                    return render(request, "usuario/login.html", contexto)
                # return HttpResponse("Usuario autenticado  id:"+str(usuario.id), request)
            except IntegrityError:
                contexto = {
                    "mensaje": "Error en credenciales de Acceso!",
                    "items_cart": "",
                }
                return render(request, "usuario/login.html", contexto)
        else:
            contexto = {
                "mensaje": "Error en datos de Acceso!",
                "items_cart": "",
            }
            return render(request, "usuario/login.html", contexto)
    else:
        contexto = {
            "mensaje": "Bienvenido, cuidado con el Dog!",
            "items_cart": "",
        }
        return render(request, "usuario/login.html", contexto)
    

@login_required(login_url="/iniciar_sesion")
@csrf_protect
def perfil(request):
    nivel = 1
    u = None
    mensaje2 = ""
    cla_mensaje2 = ""
    if request.method == "POST":
        # Segundo Nivel
        nivel = 2
        if (
            "cuenta" in request.POST
            and "nombres" in request.POST
            and "apellidos" in request.POST
            and "email" in request.POST
        ):
            try:
                # Actualizar los datos en la tabla
                u = User.objects.get(pk=request.user.id)
                u.username = request.POST["cuenta"]
                u.first_name = request.POST["nombres"]
                u.last_name = request.POST["apellidos"]
                u.email = request.POST["email"]
                u.save()
                mensaje2 = "Datos actualizados exitosamente!"
                cla_mensaje2 = "alert-success"
                return HttpResponseRedirect("/", request)

            except IntegrityError:
                mensaje2 = "Error: no se actualizaron los datos!"
                cla_mensaje2 = "alert-danger"
        else:
            # Error por falta de variables/datos necesarias
            mensaje2 = "No se actualiza la información por falta de datos!"
            cla_mensaje2 = "alert-warning"
    else:
        # Primer Nivel
        # u = User.objects.get(username="john")
        u = User.objects.get(pk=request.user.id)

    contexto = {
        "mensaje": "Actualización del perfil",
        "usuario": u,
        "nivel": nivel,
        "mensaje2": mensaje2,
        "cla_mensaje2": cla_mensaje2,
        # "items_cart": items_cart,
    }
    return render(request, "usuario/perfil.html", contexto)


@login_required(login_url="/iniciar_sesion")
@csrf_protect
def cambiar_clave(request):
    nivel = 1
    u = None
    mensaje2 = ""
    cla_mensaje2 = ""
    if request.method == "POST":
        # Segundo Nivel
        nivel = 2
        if (
            "clave" in request.POST
            and "clave1" in request.POST
            and "clave2" in request.POST
        ):
            try:
                # Actualizar los datos en la tabla
                if request.POST["clave1"] == request.POST["clave2"]:
                    if request.user.check_password(request.POST["clave"]):
                        u = User.objects.get(pk=request.user.id)
                        u.set_password(request.POST["clave1"])
                        u.save()
                        usuario = auth.authenticate(
                            username=request.user, password=request.POST["clave1"]
                        )
                        auth.login(request, usuario)
                        mensaje2 = "Se actualizó la contraseña exitosamente!"
                        cla_mensaje2 = "alert-success"
                    else:
                        mensaje2 = "Error: no se actualizó la contraseña!"
                        cla_mensaje2 = "alert-danger"
                else:
                    mensaje2 = "Error en confirmación de la contraseña!"
                    cla_mensaje2 = "alert-danger"
            except IntegrityError:
                mensaje2 = "Error: no se actualizó la contraseña!"
                cla_mensaje2 = "alert-danger"
        else:
            # Error por falta de variables/datos necesarias
            mensaje2 = "No se actualiza la contraseña por falta de datos!"
            cla_mensaje2 = "alert-warning"
    else:
        # Primer Nivel
        pass
    contexto = {
        "mensaje": "Cambiar la contraseña",
        "nivel": nivel,
        "mensaje2": mensaje2,
        "cla_mensaje2": cla_mensaje2,
    }
    return render(request, "usuario/cambiar_clave.html", contexto)


@login_required(login_url='/shop/iniciar_sesion')
def cerrar_sesion(request):
	#return HttpResponse("Cerrando Sesión en mi Proyecto Tienda virtual", request)
	auth.logout(request)
	return HttpResponseRedirect("/", request)

@login_required(login_url='/shop/iniciar_sesion')
def publicaciones(request):
    try:
        id= request.user.id 
        print("ID del usuario:{}".format(id))
        cl = UserClient.objects.filter(usuario_id=id) 
        var = []
        for x in cl:
            # print(x.cliente.id)
            var.append(x.cliente.id)   
        public = Publicaciones.objects.filter(cliente_id__in=var)
        return render(request, "publicaciones/indice.html", {"public": public})
    except:
        mensaje = "No hay datos"
        contexto = {"Errorr": mensaje}
        return render(request, "publicaciones/indice.html", contexto)
    
def editar_pub(request, id):
    nivel = 1
    x = request.user.id 
    usuario = x
    p = None
    mensaje2 = ""
    cla_mensaje2 = ""
    if request.method == "POST":
        # segundo nivel
        nivel = 2
        if (
            "producto" in request.POST
            and "precio" in request.POST
            and "comentarios" in request.POST
        ):
            try:
                # actualizar datos de tabla              
                p = Publicaciones.objects.get(pk=id)
                p.producto = request.POST["producto"]
                p.precio = request.POST["precio"]
                p.comentarios = request.POST["comentarios"]
               
                if request.FILES:
                    if request.FILES["foto"]:
                        print(request.FILES["foto"])
                        p.foto_raw = request.FILES["foto"]
                    else:
                        mensaje2 = "No se actualizan fotos!"
                p.save()
                mensaje2 = "Datos actualizados exitosamente!"
                cla_mensaje2 = "alert-success"
                return HttpResponseRedirect("/publicaciones", request)
            except IntegrityError:
                mensaje2 = "Error: no se actualizaron los datos!"
                cla_mensaje2 = "alert-danger"
        else:
            mensaje2 = "No se actualiza la información por falta de datos!"
            cla_mensaje2 = "alert-warning"
    else:
        # Primer Nivel
        # p = Publicaciones.objects.get(pk=request.publicaciones.id)
        p = Publicaciones.objects.get(id=id)
        contexto = {
            "mensaje": "Actualización del perfil",
            "usuario": x,
            "public": p,
            "nivel": nivel,
            "mensaje2": mensaje2,
            "cla_mensaje2": cla_mensaje2,
        }
    return render(request, "publicaciones/editar_pub.html", contexto)

# def crear_pub(request):
#     formulario = PublicForm(request.POST or None, request.FILES or None)
#     if formulario.is_valid():
#         formulario.save()
#         return redirect("publicaciones")
#     return render(request, "publicaciones/crear_pub.html", {"formulario": formulario})

def eliminar_pub(request, id):
      p = Publicaciones.objects.get(pk=id)
    #   public = get_object_or_404(Publicaciones, id=id) # type: ignore
      p.delete()
      return HttpResponseRedirect("/publicaciones", request)


def crear_pub(request):
    nivel = 1
    x = UserClient.objects.get(pk=request.user.id)
    cliente_id = x.cliente_id
    p = None
    mensaje2 = ""
    cla_mensaje2 = ""
    print("nivel 1")
    if request.method == "POST" or None:
        print("nivel = 2")
        print("nivel POST") 

        if (
            "producto" in request.POST
            and "precio" in request.POST
            and "comentarios" in request.POST
            and "foto" in request.POST
        ):
            try:
                pro = request.POST['producto']
                fec = request.POST['fecha_publicacion']
                print(fec)
                fecObj = datetime.strptime(fec, "%Y-%m-%dT%H:%M")
                print(type(fec))
                fecObj = fecObj.replace(tzinfo=pytz.timezone('America/Bogota'))
                print(fec)
                print(fecObj)
                pre = request.POST['precio']
                com = request.POST['comentarios']
                print(request)
                print("-----")
                print(request.FILES)
                if request.FILES["foto"]:
                        print(request.FILES["foto"])
                parent_images_path = '/'.join(['static', 'imagenes'])
                fot = request.POST['foto']          
                # fot = '/'.join([parent_images_path, fot])  
                # pub = Publicaciones.objects.create(producto=pro, fecha_publicacion=fecObj, precio=pre, comentarios=com, foto_raw= request.FILES["foto"], cliente_id=cliente_id)
                pub = Publicaciones.objects.create(producto=pro, fecha_publicacion=fecObj, precio=pre, comentarios=com, foto_raw= fot, cliente_id=cliente_id)
                pub.save()
                mensaje2 = "Datos actualizados exitosamente!"
                cla_mensaje2 = "alert-success"
                contexto = "hola"
                print("Grabado")
                return HttpResponseRedirect("/publicaciones/", request )
            except IntegrityError:
                mensaje2 = "Error: no se crearon los los datos!"
                cla_mensaje2 = "alert-danger"
                print(mensaje2)
                print(traceback.format_exc())
            except:
                print("Error desconocido detectado")
                print(traceback.format_exc())
        else:
            mensaje2 = "No se actualiza la información por falta de datos!"
            cla_mensaje2 = "alert-warning"

    else:
        # Primer Nivel
        print("else nivel 1")
        print ( x ) 
        print ( x.cliente_id )
        contexto = {
            "mensaje": "Actualización del perfil",
            "usuario": x,
            "cliente_id": cliente_id,
            "public": p,
            "nivel": nivel,
            "mensaje2": mensaje2,
            "cla_mensaje2": cla_mensaje2,
        }
        return render(request, "publicaciones/crear_pub.html", contexto)   



####
def nosotros(request, id):
    print(id)
    nos= Clientes.objects.filter(id=id)
    contexto= {"nosotros": nos}
    return render(request, "warehouses/nosotros.html", contexto)