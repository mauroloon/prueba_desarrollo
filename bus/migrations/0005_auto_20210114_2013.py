# Generated by Django 3.1.5 on 2021-01-14 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0004_chofer_estado_pasajeros_persona_promediotrayectosreservas_reservapasajero_trayecto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promediotrayectosreservas',
            options={'ordering': ['PTR_ID'], 'verbose_name': 'Promedio', 'verbose_name_plural': 'Promedios'},
        ),
        migrations.AlterModelOptions(
            name='trayecto',
            options={'ordering': ['TYO_ID'], 'verbose_name': 'Trayecto', 'verbose_name_plural': 'Trayectos'},
        ),
    ]
