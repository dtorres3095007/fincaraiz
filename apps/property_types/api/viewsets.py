from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from ..models import PropertyType
from .serializers import PropertyTypeSerializer
import datetime

class GetPropertyTypes(viewsets.ViewSet):
    def list(self, request):
        queryset = PropertyType.objects.all().order_by('slug')
        serializer = PropertyTypeSerializer(queryset, many=True)
        return Response(serializer.data)

class addPropertyType(generics.CreateAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer

    def create(self, request, *args, **kwargs):
        super(addPropertyType, self).create(request, args, kwargs)
        return Response({"message": "Success"})

class DetailPropertyType(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
