from .models import Property
from rest_framework import viewsets, permissions
from .serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertySerializer
