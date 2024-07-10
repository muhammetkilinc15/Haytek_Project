from rest_framework import serializers
from Dingtion.models import *


class RelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Relay
        fields = '__all__'
    

class DeviceSerializer(serializers.ModelSerializer):
    relays = serializers.SerializerMethodField()
    class Meta:
        model = Device
        fields = ('id','model','ip','port','relays','created_date',)
        
    def get_relays(self, obj):
        # Örnek olarak, relays'leri id'ye göre sıralı şekilde getiriyoruz
        relays_qs = Relay.objects.filter(device=obj).order_by('relay_id')
        serializer = RelaySerializer(instance=relays_qs, many=True)
        return serializer.data