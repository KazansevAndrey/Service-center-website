from rest_framework import routers
from .views import RegistrationView, CurrentUserView, CookieTokenRefreshView, CookieTokenObtainPairView
from django.urls import path
router = routers.DefaultRouter()



urlpatterns = (
    path('registration', RegistrationView.as_view(), name='user-registration'),
    path('current_user', CurrentUserView.as_view(), name='current_user'),
    path('auth/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    )