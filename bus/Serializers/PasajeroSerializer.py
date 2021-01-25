from rest_framework import serializers
from bus.models import Pasajeros

class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajeros
        fields = ('PSR_ID','PSR_N_RESERVA','PRS_ID','VJE_ID','PSR_VIGENCIA')
        depth = 1
