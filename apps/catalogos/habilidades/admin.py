from django.contrib import admin
from apps.catalogos.habilidades.models import Habilidades

# Register your models here.
@admin.register(Habilidades)
class HabilidadesAdmin(admin.ModelAdmin):
    search_fields = ['Codigo', 'Nombre_Habilidad']
    list_display = ['Codigo', 'Nombre_Habilidad']
