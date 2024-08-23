from rest_framework import routers
from .views import CertificatesViewSet
router = routers.DefaultRouter()

router.register('', CertificatesViewSet)

urlpatterns = router.urls