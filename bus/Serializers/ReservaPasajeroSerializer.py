from rest_framework import serializers
from bus.models import ReservaPasajero

class ReservaPasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaPasajero
        fields = ('RSV_ID', 'TYO_ID', 'FDT_DIA_INICIO', 'FDT_DIA_LLEGADA', 'BUS_ID', 'CFR_ID', 'EST_ID', 'RSV_VIGENCIA')
        depth = 1
