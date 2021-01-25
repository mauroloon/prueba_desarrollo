from django.db import models
from bus.models.Persona import Persona
from bus.models.ReservaPasajero import ReservaPasajero

#vje_id = rsv_id
class Pasajeros(models.Model):
    PSR_ID = models.AutoField(primary_key=True)
    PSR_N_RESERVA = models.IntegerField()
    PRS_ID = models.ForeignKey(Persona, on_delete=models.CASCADE)
    VJE_ID = models.ForeignKey(ReservaPasajero, on_delete=models.CASCADE)
    PSR_VIGENCIA = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Pasajero"
        verbose_name_plural = 'Pasajeros'
        ordering = ['PSR_ID']

    def __str__(self):
        return str(self.PSR_ID)
