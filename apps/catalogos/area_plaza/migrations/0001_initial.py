# Generated by Django 4.2 on 2024-09-25 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaPlaza',
            fields=[
                ('ID_AreaPLAZA', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo', models.CharField(max_length=16, unique=True, verbose_name='Código')),
                ('Descripcion', models.CharField(max_length=500, verbose_name='Descripcion')),
                ('ID_Cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cargo.cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Area de Plaza',
            },
        ),
    ]
