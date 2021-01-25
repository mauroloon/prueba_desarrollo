from django.db import models

class Trayecto (models.Model):
    TYO_ID = models.AutoField(primary_key=True)
    LGR_ID_INICIO = models.IntegerField()
    LGR_ID_TERMINO = models.IntegerField()
    TYO_VIGENCIA = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Trayecto"
        verbose_name_plural = 'Trayectos'
        ordering = ['TYO_ID']

    def __str__(self):
        return str(self.TYO_ID)