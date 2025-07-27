
from rest_framework import serializers
from .models import Menu
from .models import Booking
from django.contrib.auth.models import User
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=['Title','Price','Inventory']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['Name','No_of_guests','BookingDate']        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']          