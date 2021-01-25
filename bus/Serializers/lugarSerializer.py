from rest_framework import serializers
from bus.models import Lugar

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ('LGR_ID','LGR_NOMBRE','LGR_DESCRIPCION')        
