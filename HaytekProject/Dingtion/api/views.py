from rest_framework import generics, status
from rest_framework.response import Response
from  Dingtion.models import *
from Dingtion.api.serializers import *


# Burada izin sınıflarını içe aktarıyoruz
from rest_framework.permissions import IsAuthenticated
from Dingtion.api.permissions import IsAdminUserOrAuthorizedUser
#! ********** Device Views **********

class DeviceList(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminUserOrAuthorizedUser]

class DeviceCreate(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminUserOrAuthorizedUser]

class DeviceRetrieve(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminUserOrAuthorizedUser]

class DeviceUpdate(generics.UpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminUserOrAuthorizedUser]

class DeviceDelete(generics.DestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminUserOrAuthorizedUser]

#! ********** Relay Views **********

class RelayList(generics.ListAPIView):
    queryset = Relay.objects.all().order_by('relay_id')
    serializer_class = RelaySerializer
    # permission_classes =[IsAdminUserOrAuthorizedUser]

class RelayCreate(generics.CreateAPIView):
    queryset = Relay.objects.all()
    serializer_class = RelaySerializer
    permission_classes =  [IsAdminUserOrAuthorizedUser]

class RelayRetrieve(generics.RetrieveAPIView):
    queryset = Relay.objects.all()
    serializer_class = RelaySerializer
    permission_classes =  [IsAdminUserOrAuthorizedUser]

class RelayUpdate(generics.RetrieveUpdateAPIView):
    queryset = Relay.objects.all()
    serializer_class = RelaySerializer
    permission_classes = [IsAdminUserOrAuthorizedUser]  # veya uygun yetki sınıfını belirtin


class RelayDelete(generics.DestroyAPIView):
    queryset = Relay.objects.all()
    serializer_class = RelaySerializer
    permission_classes =  [IsAdminUserOrAuthorizedUser]
    
