from django.contrib import admin
from django.urls import path
from app_contactos.views import ContactoListar, ContactoDetalle, ContactoNuevo, ContactoActualizar, ContactoEliminar, CerrarSesion
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
 
    # Para mostrar todos los registros en una tabla
    path('app_contactos/', ContactoListar.as_view(template_name = "app_contactos/index.html"), name='listar'),
 
    # Para mostrar una página con el detalle del registro
    path('app_contactos/detalle/<int:pk>', ContactoDetalle.as_view(template_name = "app_contactos/detalles.html"), name='detalles'),
 
    # Para mostrar formulario de alta de nuevo registro
    path('app_contactos/nuevo', ContactoNuevo.as_view(template_name = "app_contactos/crear.html"), name='nuevo'),
 
    # Para mostrar formulario de modificación de registro
    path('app_contactos/editar/<int:pk>', ContactoActualizar.as_view(template_name = "app_contactos/actualizar.html"), name='actualizar'), 
 
    # Para eliminar un registro
    path('app_contactos/eliminar/<int:pk>', ContactoEliminar.as_view(), name='eliminar'),    

    # Para html Cerrar Sesión (sólo ejemplo para mostrar una página HTML estática)
    path('app_contactos/cerrarsesion', CerrarSesion, name='cerrarsesion'),	
]

urlpatterns += staticfiles_urlpatterns()