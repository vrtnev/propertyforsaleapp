from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        property = '__all__'
        fields = '__all__'
