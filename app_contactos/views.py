from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contactos
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

#Para obtener todos los registros de la tabla Contactos 
class ContactoListar(ListView): 
    model = Contactos

#Para obtener todos los campos de un registro de la tabla Contactos 
class ContactoDetalle(DetailView): 
    model = Contactos

#Para insertar un nuevo contacto en la tabla Contactos 
class ContactoNuevo(SuccessMessageMixin, CreateView): 
    model = Contactos
    form = Contactos
    fields = "__all__" 
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Contacto añadido correctamente.'
 
    # Redirigimos a la página principal tras insertar el registro
    def get_success_url(self):        
        return reverse('listar')
 
#Para modificar un contacto existente de la tabla Contactos
class ContactoActualizar(SuccessMessageMixin, UpdateView): 
    model = Contactos
    form = Contactos
    fields = "__all__"
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Contacto actualizado correctamente.'
 
    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('listar')

#Para eliminar un contacto de la tabla Contactos 
class ContactoEliminar(SuccessMessageMixin, DeleteView): 
    model = Contactos
    form = Contactos
    fields = "__all__"     
 
    #Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Contacto eliminado correctamente.'
        messages.success (self.request, (success_message))       
        return reverse('listar')

#Ejemplo de redirección a una página HTML existente
def CerrarSesion(request):
    return render(request, 'logout.html')		