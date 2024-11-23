from django.shortcuts import render
from rest_framework import viewsets
from .serializer import HousesSerializer, SellersSerializer, HouseSellerSerializer
from .models import Houses, Sellers, HousesSellers

# Create your views here.

class HouseViewSet(viewsets.ModelViewSet):
    serializer_class = HousesSerializer
    queryset = Houses.objects.all()
    
class SellerViewSet(viewsets.ModelViewSet):
    queryset = Sellers.objects.all()
    serializer_class = SellersSerializer

class HouseSellerViewSet(viewsets.ModelViewSet):
    queryset = HousesSellers.objects.all()
    serializer_class = HouseSellerSerializer
