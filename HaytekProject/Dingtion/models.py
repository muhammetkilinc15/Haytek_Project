from django.db import models

from django.contrib.auth.models import User



class Device(models.Model):
    model = models.CharField(max_length=100)
    ip = models.CharField(max_length=15)
    port = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Cihaz'
        verbose_name_plural = 'Cihazlar'

class Relay(models.Model):
   
    name = models.CharField(max_length=100)
    relay_id = models.IntegerField(null=True,unique=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='relays')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.device.model} - {self.name}"
    
    class Meta:
        verbose_name = 'Röle'
        verbose_name_plural = 'Röleler'


class UserDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_devices')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='user_devices')

    def __str__(self):
        return f"{self.user.username} - {self.device.model}"
    
    class Meta:
        verbose_name = 'Kullanıcı Cihazı'
        verbose_name_plural = 'Kullanıcı Cihazları'

class UserRelayPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_relay_permissions')
    relay = models.ForeignKey(Relay, on_delete=models.CASCADE, related_name='user_relay_permissions')
    can_enable = models.BooleanField(default=False)
    can_disable = models.BooleanField(default=False)
    expiration_date = models.DateField(null=True, blank=True) 

    def __str__(self):
        return f"{self.user.username} - {self.relay.name}"

    class Meta:
        verbose_name = 'Kullanıcı Cihaz İzini'
        verbose_name_plural = 'Kullanıcı Cihaz İzinleri'