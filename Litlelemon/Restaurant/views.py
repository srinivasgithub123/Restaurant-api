from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Menu
from .models import Booking
from rest_framework import generics
from .serializers import MenuSerializer
from .serializers import BookingSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

class SingleMenuView(generics.RetrieveAPIView,generics.DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer  

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    

