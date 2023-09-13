from rest_framework import serializers

from .models import person

class pSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields =('__all__')