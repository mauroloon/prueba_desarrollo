from django.db import models
from bus.models.Lugar import Lugar

class Chofer(models.Model):
    CFR_ID = models.AutoField(primary_key=True)
    CFR_NOMBRE = models.CharField(max_length=100,blank=True, null=True)
    CFR_APELLIDO = models.CharField(max_length=100,blank=True, null=True)
    CFR_RUT = models.CharField(max_length=100,blank=False, null=False)
    LGR_ID = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    CFR_VIGENCIA = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Chofer"
        verbose_name_plural = 'Choferes'
        ordering = ['CFR_ID']

    def __str__(self):
        return self.CFR_NOMBRE + ' ' + self.CFR_APELLIDO