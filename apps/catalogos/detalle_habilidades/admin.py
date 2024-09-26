from django.contrib import admin
from apps.catalogos.detalle_habilidades.models import DetalleHabilidades

# Register your models here.
@admin.register(DetalleHabilidades)
class DetalleHabilidadesAdmin(admin.ModelAdmin):
    search_fields = ['Valor']
    list_display = ['ID_Postulante','ID_Habilidades','Valor']
