from django.contrib import admin
from apps.catalogos.postulante.models import Postulante

# Register your models here.
@admin.register(Postulante)
class PostulanteAdmin(admin.ModelAdmin):
    search_fields = ['Cedula', 'Nombre_Postulante']
    list_display = ['Cedula', 'Nombre_Postulante', 'Apellidos', 'Sexo', 'Correo','Telefono','Fecha_Nacimiento','Direccion','Experiencia_Laboral', 'ID_Municipio','ID_Profesion']
