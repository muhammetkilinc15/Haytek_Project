from django.urls import path
from Dingtion.api import views as api_views
urlpatterns = [
    
    # Urls for device CRUD operaiton
    path('devicelist/',api_views.DeviceList.as_view(),name="device-list"),
    path('deviceDetail/<int:pk>',api_views.DeviceRetrieve.as_view(),name="device-detail"),
    path('deviceAdd/',api_views.DeviceCreate.as_view(),name="device-add"),
    path('deviceUpdate/<int:pk>/', api_views.DeviceUpdate.as_view(), name='device-update'),
    path('deviceDelete/<int:pk>/', api_views.DeviceDelete.as_view(), name='device-update'),
    
    # Urls for relay CRUD operaiton
    
    path('relaylist/',api_views.RelayList.as_view(),name="relay-list"),
    path('relayDetail/<int:pk>',api_views.RelayRetrieve.as_view(),name="relay-detail"),
    path('relayAdd/',api_views.RelayCreate.as_view(),name="relay-add"),
    path('relayUpdate/<int:pk>/', api_views.RelayUpdate.as_view(), name='relay-update'),
    path('relayDelete/<int:pk>/', api_views.RelayDelete.as_view(), name='relay-update'),
    
    
    
]
