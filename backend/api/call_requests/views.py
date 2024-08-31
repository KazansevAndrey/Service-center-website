from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from .models import CallRequest
from .serializers import *
from .permissions import *
# Create your views here.
# Create your views here.

class CallRequestViewSet(ModelViewSet):
    count = CallRequest.objects.count()
    queryset = CallRequest.objects.all().order_by('-time_create')
    serializer_class = CallRequestSerializer
    permission_classes = (CallRequestPermission,)