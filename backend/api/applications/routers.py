from rest_framework import routers
from django.urls import path
from .views import *
router = routers.DefaultRouter()
router.register(r'client-applications', ClientApplicationViewSet, basename='client-applications')
router.register(r'incoming-repair-applications', IncomingRepairApplicationViewSet, basename='incoming-repair-applications')
router.register(r'current-repair-applications', CurrentRepairApplicationViewSet, basename='current-repair-applications')
router.register(r'personal-repair-applications', PersonalRepairApplicationViewSet, basename='personal-repair-applications')
router.register(r'archive-repair-applications', ArchiveRepairApplicationViewSet, basename='archive-repair-applications')
router.register(r'retrieve-applicaitons', RetrieveApplicationViewSet, basename='retrieve-applications')
router.register(r'accept-application', AcceptApplicationByEmployee, basename = 'access-appplication')
urlpatterns = router.urls
urlpatterns+=[path('device-types-list', DevicesTypesList.as_view(), name='device-types-list'),
]
