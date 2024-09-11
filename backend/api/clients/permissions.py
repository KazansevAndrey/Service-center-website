from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    """Доступ к списку клиентов и отдельному клиенту"""

    def has_permission(self, request, view):
        return request.user.is_superuser
     
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser
