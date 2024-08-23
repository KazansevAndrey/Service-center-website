from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissons import *
# Create your views here.

class ServicesViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [SerivesPermission]

class ServicesCategoryViewSet(ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServicesCategorySerializer
    permission_classes = [SerivesPermission]

class PopularServicesByCategoryList(APIView):

    def get(self, request, category_id,  format=None):
        print(category_id)
        services = Service.objects.filter(category_id=category_id, is_popular=True)
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data)

class AnotherServicesByCategoryList(APIView):

    def get(self, request, category_id,  format=None):
        services = Service.objects.filter(category_id=category_id, is_popular=False)
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data)