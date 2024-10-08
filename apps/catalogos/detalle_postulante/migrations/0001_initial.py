# Generated by Django 4.2 on 2024-09-25 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postulante', '0001_initial'),
        ('detalle_plaza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePostulante',
            fields=[
                ('ID_DETALLE_POSTULANTE', models.AutoField(primary_key=True, serialize=False)),
                ('Valor', models.CharField(max_length=50, verbose_name='Valor')),
                ('ID_DetallePlaza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='detalle_plaza.detalleplaza')),
                ('ID_Postulante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='postulante.postulante')),
            ],
            options={
                'verbose_name': 'Detalle Postulante',
            },
        ),
    ]
