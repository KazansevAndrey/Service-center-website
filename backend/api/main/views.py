from rest_framework import viewsets
from .models import Certificates
from .serializers import CertificatesSerializer
# Create your views here.

class CertificatesViewSet(viewsets.ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer
