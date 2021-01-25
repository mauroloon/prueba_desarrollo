# Generated by Django 3.1.5 on 2021-01-14 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('LGR_ID', models.AutoField(primary_key=True, serialize=False)),
                ('LGR_NOMBRE', models.CharField(max_length=100)),
                ('LGR_DESCRIPCION', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
                'ordering': ['LGR_ID'],
            },
        ),
    ]
