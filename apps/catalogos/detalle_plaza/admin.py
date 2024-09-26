from django.contrib import admin
from apps.catalogos.detalle_plaza.models import DetallePlaza

# Register your models here.
@admin.register(DetallePlaza)
class DetallePlazaAdmin(admin.ModelAdmin):
    search_fields = ['Valor']
    list_display = ['Valor']
