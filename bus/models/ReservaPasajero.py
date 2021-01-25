from django.db import models
from bus.models.Bus import Bus
from bus.models.Chofer import Chofer
from bus.models.Estado import Estado
from bus.models.Trayecto import Trayecto

class ReservaPasajero(models.Model):
    RSV_ID = models.AutoField(primary_key=True)
    TYO_ID = models.ForeignKey(Trayecto, on_delete=models.CASCADE)
    FDT_DIA_INICIO = models.DateTimeField(auto_now=False)
    FDT_DIA_LLEGADA = models.DateTimeField(auto_now=False)
    BUS_ID = models.ForeignKey(Bus, on_delete=models.CASCADE)
    CFR_ID = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    EST_ID = models.ForeignKey(Estado, on_delete=models.CASCADE)
    RSV_VIGENCIA = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = 'Reservas'
        ordering = ['RSV_ID']

    def __str__(self):
        return 'reserva ' + str(self.RSV_ID)