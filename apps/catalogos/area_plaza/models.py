from django.db import models
from apps.catalogos.cargo.models import Cargo

# Create your models here.
class AreaPlaza(models.Model):
    ID_AreaPLAZA = models.AutoField(primary_key=True)
    Codigo = models.CharField(verbose_name='Código', max_length=16, unique=True)
    Descripcion = models.CharField(verbose_name='Descripcion', max_length=500)
    ID_Cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, verbose_name='Cargo')

    class Meta:
        verbose_name = 'Area de Plaza'

    def __str__(self):
        return f"{self.Codigo} - {self.Descripcion}"

