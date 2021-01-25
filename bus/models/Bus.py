from django.db import models
from bus.models.Lugar import Lugar

class Bus(models.Model):
    BUS_ID = models.AutoField(primary_key=True)
    BUS_MARCA = models.CharField(max_length=50, blank=True, null=True)
    BUS_MODELO = models.CharField(max_length=100, blank=True, null=True)
    BUS_VIGENCIA = models.IntegerField(default=1)
    LGR_ID = models.ForeignKey(Lugar, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Bus"
        verbose_name_plural = 'Buses'
        ordering = ['BUS_ID']

    def __str__(self):
        return self.BUS_MARCA + ' ' + self.BUS_MODELO + '_' + str(self.BUS_ID)
