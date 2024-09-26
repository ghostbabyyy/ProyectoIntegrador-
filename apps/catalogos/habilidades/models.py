from django.db import models

# Create your models here.
class Habilidades(models.Model):
    ID_Habilidade = models.AutoField(primary_key=True)
    Codigo = models.CharField(verbose_name='Código', max_length=20, unique=True)
    Nombre_Habilidad =models.CharField(verbose_name='Nombre Habilidad', max_length=100)

    class Meta:
        verbose_name = 'Habilidade'

    def __str__(self):
        return f'{self.Codigo} {self.Nombre_Habilidad}'
