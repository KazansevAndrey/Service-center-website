from rest_framework import routers
from django.urls import path
from .views import ClientApplicationViewSet, IncomingRepairApplicationViewSet, CurrentRepairApplicationViewSet, DevicesTypesList
router = routers.DefaultRouter()
router.register(r'client-applications', ClientApplicationViewSet, basename='client-applications')
router.register(r'incoming-repair-applications', IncomingRepairApplicationViewSet, basename='incoming-repair-applications')
router.register(r'current-repair-applications', CurrentRepairApplicationViewSet, basename='current-repair-applications')

urlpatterns = router.urls
urlpatterns+=[path('device-types-list', DevicesTypesList.as_view(), name='device-types-list')]
