from django.db.models.signals import post_save
from django.dispatch import receiver
from Dingtion.models import Relay
import requests

# Yapılan istek ile 

@receiver(post_save, sender=Relay)
def relay_status_changed(sender, instance, created, **kwargs):
    if not created:  # Sadece güncelleme durumunda işlem yapmak istiyoruz
        # İlgili Device'ın ip ve port bilgilerini alıyoruz
        device = instance.device  # Relay modelindeki ilişkili Device
        url = f'http://{device.ip}:{device.port}/relay_cgi.cgi'
        
        # HTTP isteği için parametreleri hazırlıyoruz
        params = {
            'type': '0',
            'relay': instance.relay_id,  # Relay modelindeki uygun alanı kullanın
            'on': '1' if instance.is_active else '0',
            'time': '0',
            'pwd': '0',
        }
        
        # HTTP GET isteği gönderiyoruz
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Hata varsa raise edilir
            print(f'Relay durumu başarıyla güncellendi: {instance}')
        except requests.exceptions.RequestException as e:
            print(f'Relay durumu güncellenirken hata oluştu: {e}')