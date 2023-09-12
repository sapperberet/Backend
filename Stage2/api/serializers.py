from rest_framework import serializers

from .models import Item,Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields =('__all__')
    
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields =('__all__')
    