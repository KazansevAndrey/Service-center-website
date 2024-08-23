from rest_framework import routers
from django.urls import path
from .views import *
router = routers.DefaultRouter()
router.register('services-list', ServicesViewSet, basename='services-list')
router.register('services-category-list', ServicesCategoryViewSet, basename='services-category-list')

urlpatterns = router.urls+[
    path('popular-services-by-category-list/<int:category_id>/', PopularServicesByCategoryList.as_view(), name='popular-services-by-category-list'),
    path('another-services-by-category-list/<int:category_id>/', AnotherServicesByCategoryList.as_view(), name='another-services-by-category-list')]
