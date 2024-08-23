from rest_framework import permissions

class CallRequestPermission(permissions.BasePermission):
    '''Ограничения заявок на звонки'''
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user.is_superuser
        elif request.method == 'POST':
            return True
        else:
            return request.user.is_superuser
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser