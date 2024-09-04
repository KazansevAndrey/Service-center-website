from rest_framework import permissions

class IsEmployee(permissions.BasePermission):
    """
    Доступ только сотрудникам
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'employeeprofile')
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return hasattr(request.user, 'employeeprofile') 
        else:
            return obj.employee.user == request.user
    
class IsEmployeeAccessApplication(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'PATCH':
            return True
        
class IsClient(permissions.BasePermission):
    """
    Клиентский доступ
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return True
        
    def has_object_permission(self, request, view, obj):
        return False
         
