from rest_framework import serializers
from bus.models import Trayecto

class TrayectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trayecto
        fields = ('TYO_ID','LGR_ID_INICIO','LGR_ID_TERMINO','TYO_VIGENCIA')
