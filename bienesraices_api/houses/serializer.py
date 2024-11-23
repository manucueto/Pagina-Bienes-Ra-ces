from rest_framework import serializers
from .models import Houses, Sellers, HousesSellers

class HousesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = '__all__'

class SellersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellers
        fields = '__all__'

class HouseSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousesSellers
        fields = '__all__'