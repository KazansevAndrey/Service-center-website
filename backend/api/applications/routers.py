from rest_framework import routers
from django.urls import path
from .views import ClientApplicationViewSet, EmployeeApplicationViewSet, DevicesTypesList
router = routers.DefaultRouter()
router.register(r'client-applications', ClientApplicationViewSet, basename='client-applications')
router.register(r'employee-applications', EmployeeApplicationViewSet, basename='employee-applications')

urlpatterns = router.urls
urlpatterns+=[path('device-types-list', DevicesTypesList.as_view(), name='device-types-list')]
