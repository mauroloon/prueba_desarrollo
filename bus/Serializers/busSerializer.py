from rest_framework import serializers
from bus.models import Bus

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('BUS_ID', 'BUS_MARCA', 'BUS_MODELO', 'BUS_VIGENCIA','LGR_ID')
        depth = 1
