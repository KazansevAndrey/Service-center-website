from rest_framework import routers
from .views import RegistrationView, CurrentUserView
from django.urls import path
router = routers.DefaultRouter()



urlpatterns = (
    path('registration', RegistrationView.as_view(), name='user-registration'),
    path('current_user', CurrentUserView.as_view(), name='current_user'))