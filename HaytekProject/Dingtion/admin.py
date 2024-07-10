from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from Dingtion.models import *

class MyAdminSite(AdminSite):
    site_header = "Haytek Uzaktan Cihaz Yönetim Paneli"
    site_title = "Haytek Admin Portal"
    index_title = "Haytek Admin Hoşgeldiniz"

admin_site = MyAdminSite(name='myadmin')

class RelayAdmin(admin.ModelAdmin):
    list_display = ('name', 'device', 'is_active')
    search_fields = ('custom_relay_id',)  # Özel filtreleme alanı ekleniyor
    list_per_page = 8
    ordering = ('relay_id',)  # Sıralama yapmak için ordering kullanın
    def custom_relay_id(self, obj):
        if obj.relay_id == self.relay_id:
            return obj.relay_id + 1  # relay_id'nin bir fazlasını döndür
        return obj.relay_id
    custom_relay_id.short_description = 'Custom Relay ID'

# Kullanıcı ve Grup modellerini kayıt edin
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Device)
admin_site.register(Relay,RelayAdmin)
admin_site.register(UserDevice)
admin_site.register(UserRelayPermission)
