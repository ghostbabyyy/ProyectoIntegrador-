from django.contrib import admin
from apps.catalogos.lista_detalle.models import ListaDetalle

# Register your models here.
@admin.register(ListaDetalle)
class ListaDetalleAdmin(admin.ModelAdmin):
    search_fields = ['Codigo', 'Nombre']
    list_display = ['Codigo', 'Nombre', 'Descripcion', 'Fecha_Creacion']
