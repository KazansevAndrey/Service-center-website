from rest_framework import permissions

class CertificatesPermission(permissions.BasePermission):
    '''Ограничения доступа к фото сертификатов'''
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return request.user.is_superuser
        
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return request.user.is_superuser