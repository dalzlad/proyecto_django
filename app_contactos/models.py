from django.db import models
from django.utils import timezone

# Clase "Contactos" que tendrá los campos que se usarán en la aplicación y que se crearán en la tabla la base de datos
class Contactos(models.Model):
	nombre = models.CharField(max_length=150, null=False, verbose_name="Nombre", default="")
	telefono_movil = models.CharField(max_length=9, null=True, blank=True, verbose_name="Tlfno. móvil", default="")
	telefono_fijo = models.CharField(max_length=9, null=True, blank=True, verbose_name="Tlfno. fijo", default="+34")
	mail = models.EmailField(max_length=150, null=True, blank=True, verbose_name="EMail", default="")
	direccion = models.CharField(max_length=200, null=True, blank=True, verbose_name="Dirección postal", default="")	
	#foto = models.FileField(upload_to ='fotos/', max_length=254, null=True, blank=True, verbose_name="Foto")
	foto = models.FileField(max_length=254, null=True, blank=True, verbose_name="Foto")
	empresa = models.CharField(max_length=150, default='Proyecto A')
	fecha_alta = models.DateTimeField(auto_now_add=True)
	fecha_actualizacion = models.DateTimeField(auto_now=True)
 
	class Meta:
		 db_table = 'contactos' # Nombre que tendrá la tabla que se creará en la base de datos en la Base de Datos