from django.contrib.auth import login
from rest_framework import permissions
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from yaml import serialize
from .serializers import UserSerializer
# Create your views here.

class RegistrationView(generics.CreateAPIView):

    permission_classes = [
        permissions.AllowAny]
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user