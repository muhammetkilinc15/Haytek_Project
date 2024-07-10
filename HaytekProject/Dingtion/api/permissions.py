from rest_framework import permissions
from Dingtion.models import UserRelayPermission
from Dingtion.models import Relay
class IsAdminUserOrAuthorizedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.user.is_staff:  # Eğer kullanıcı adminse, doğrudan izin ver
            return True
        
        # Diğer durumda, röle id'sini alın ve izin kontrolü yapın
        relay_id = view.kwargs.get('pk')  # pk değerini al
        try:
            relay = Relay.objects.get(pk=relay_id)
            permission = UserRelayPermission.objects.get(user=request.user, relay=relay)
        except (Relay.DoesNotExist, UserRelayPermission.DoesNotExist):
            return False
        
        # Kullanıcı izni kontrolü
        if permission.can_enable or permission.can_disable:
            return True
        
        return False
