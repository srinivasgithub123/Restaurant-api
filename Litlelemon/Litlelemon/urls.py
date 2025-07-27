"""
URL configuration for Litlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Restaurant import views
from django.contrib.auth.models import User
from rest_framework import viewsets
from Restaurant.serializers import UserSerializer  # Ensure this import matches your structure

# Create a router and register the BookingViewSet and UserViewSet
router = DefaultRouter()
router.register('tables', views.BookingViewSet)  # Ensure views.BookingViewSet is correct

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router.register('users', UserViewSet)    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Restaurant.urls')),  # Ensure this file has its own URL patterns
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
