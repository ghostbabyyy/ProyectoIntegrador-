from django.db import models
from apps.catalogos.postulante.models import Postulante
from apps.catalogos.detalle_plaza.models import DetallePlaza

# Create your models here.
class DetallePostulante(models.Model):
    ID_DETALLE_POSTULANTE = models.AutoField(primary_key=True)
    Valor = models.CharField(verbose_name="Valor", max_length=50)
    ID_Postulante = models.ForeignKey(Postulante, on_delete=models.PROTECT)
    ID_DetallePlaza = models.ForeignKey(DetallePlaza, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Detalle Postulante"

    def __str__(self):
        return self.Valor
