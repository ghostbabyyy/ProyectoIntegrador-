from django.db import models

# Create your models here.
class ListaDetalle(models.Model):
    ID_LISTA_DETALLE = models.AutoField(primary_key=True)
    Codigo = models.CharField(verbose_name="Código", max_length=20)
    Nombre = models.CharField(verbose_name="Nombre", max_length=100)
    Descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    Fecha_Creacion = models.DateField(verbose_name= "Fecha Creación")

    class Meta:
        verbose_name = "Lista de Detalle"

    def __str__(self):
        return f"{self.Codigo} {self.Nombre}"