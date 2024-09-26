from django.db import models
from apps.catalogos.plaza.models import Plaza
from apps.catalogos.lista_detalle.models import ListaDetalle

# Create your models here.
class DetallePlaza(models.Model):
    ID_DetallePlaza = models.AutoField(primary_key=True)
    Valor = models.CharField(verbose_name="Valor", max_length=50)

    class Meta:
        verbose_name = "Detalle Plaza"

    def __str__(self):
        return self.Valor
