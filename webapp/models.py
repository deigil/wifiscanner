from django.db import models

# Create your models here.
class WifiData(models.Model):
    ssid = models.CharField(max_length=255)
    bssid = models.CharField(max_length=255)
    authType = models.CharField(max_length=255)
    signalStrength = models.CharField(max_length=255)
    connectionScore = models.IntegerField()
    networkHash = models.CharField(max_length=255)

    def __str__(self):
        return self.ssid #or any field that represents the object when printed