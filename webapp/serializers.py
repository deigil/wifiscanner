# webapp/serializers.py
from rest_framework import serializers
from .models import WifiData

class WifiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WifiData
        fields = ['ssid', 'bssid', 'authType', 'signalStrength', 'connectionScore', 'networkHash']
