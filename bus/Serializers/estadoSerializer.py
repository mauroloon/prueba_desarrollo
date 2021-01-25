from rest_framework import serializers
from bus.models import Estado

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('EST_ID', 'EST_NOMBRE')
