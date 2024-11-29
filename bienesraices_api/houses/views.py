from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
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
    
    
## Custom Endpoints
@api_view(['POST'])
def massive_create(request):
    houses_data = request.data
    if not isinstance(houses_data, list):
        return Response({"error": "Expected a list of houses"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = HousesSerializer(data=houses_data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
