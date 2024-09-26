from django.db import models
from apps.catalogos.postulante.models import Postulante
from apps.catalogos.habilidades.models import Habilidades

# Create your models here.
class DetalleHabilidades(models.Model):
    ID_DetalleHabilidades = models.AutoField(primary_key=True)
    ID_Postulante = models.ForeignKey(Postulante, on_delete=models.PROTECT)
    ID_Habilidades = models.ForeignKey(Habilidades, on_delete=models.PROTECT)
    Valor = models.CharField(verbose_name="Valor", max_length=100)

    class Meta:
        verbose_name = 'Detalle Habilidades'

    def __str__(self):
        return self.Valor
