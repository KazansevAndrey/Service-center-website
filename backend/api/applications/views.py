
from urllib import request
from django.views import generic
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Application, DeviceType
from .serializers import *
from .permissions import *
# Create your views here.


class PersonalRepairApplicationViewSet(    
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = RepairApplicationSerializer
    permission_classes = [IsEmployee]

    def get_queryset(self):
        print(self.request.user)
        return Application.objects.filter(employee__user=self.request.user)
    
class IncomingRepairApplicationViewSet(
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Application.objects.filter(status='C')
    serializer_class = RepairApplicationSerializer
    permission_classes = [IsEmployee]

    # def perform_destroy(self, instance):
    #     instance.is_archived=True
    #     instance.save()

class CurrentRepairApplicationViewSet(mixins.ListModelMixin,
                                      GenericViewSet):
    queryset = Application.objects.exclude(status='C')
    serializer_class = CurrentRepairApplicationSerializer

class ArchiveRepairApplicationViewSet(
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Application.objects.filter(is_archive=True)
    serializer_class = RepairApplicationSerializer
    permission_classes = [IsEmployee]


class ClientApplicationViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = ApplicationClientSerializer
    permission_classes = [IsAuthenticated, IsClient]
    def get_queryset(self):
        return Application.objects.filter(client=self.request.user).order_by('-time_update')
    
    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
        
class DevicesTypesList(APIView):

    def get(self, request, format=None):
        device_types = DeviceType.objects.all()
        serializer = DeviceTypesSerializer(device_types, many=True)
        return Response(serializer.data)


# class ApplicationApiView(APIView):

#     def get(self, request):
#         applications = Application.objects.all()
#         print(applications)
#         return Response({'applications': ApplicationSerializer(applications, many=True).data})
    
#     def post(self, request):
        
#         serializer = ApplicationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'POST': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error":"method PUT not allowed"})
        
#         try:
#             instance = Application.objects.get(pk=pk)
#         except:
#             return Response({"error": "object does not exist"})
        
#         serializer = ApplicationSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'PUT': serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         print(pk)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         try:
#             instance = Application.objects.get(pk=pk)
#             print(instance)
#             instance.delete()
#         except:
#             return Response({"error": "object does not exist"})
        
#         return Response({"DELETE": "delete application " + str(pk)})