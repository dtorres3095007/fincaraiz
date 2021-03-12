from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from ..models import City
from .serializers import CitySerializer
import datetime

class GetCities(viewsets.ViewSet):
    def list(self, request):
        queryset = City.objects.all().order_by('slug')
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

class addCity(generics.CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def create(self, request, *args, **kwargs):
        super(addCity, self).create(request, args, kwargs)
        return Response({"message": "Success"})

class DetailCity(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
