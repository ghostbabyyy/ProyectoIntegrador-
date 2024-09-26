from django.contrib import admin
from apps.catalogos.detalle_postulante.models import DetallePostulante


# Register your models here.
@admin.register(DetallePostulante)
class DetallePostulanteAdmin(admin.ModelAdmin):
    search_fields = ['Valor']
    list_display = ['ID_Postulante','ID_DetallePlaza','Valor']
