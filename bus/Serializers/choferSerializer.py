from rest_framework import serializers
from bus.models import Chofer

class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = ('CFR_ID', 'CFR_NOMBRE','CFR_APELLIDO','CFR_RUT','LGR_ID','CFR_VIGENCIA')
        depth = 1
