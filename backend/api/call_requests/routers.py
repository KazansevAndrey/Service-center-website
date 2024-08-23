from rest_framework import routers
from .views import CallRequestViewSet

router = routers.DefaultRouter()

router.register('', CallRequestViewSet, basename='call-requests-list')

urlpatterns = router.urls