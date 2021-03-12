from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Property
from .serializers import PropertySerializer
import datetime


class GetProperties(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    def list(self, request):
        queryset = Property.objects.all().order_by('title')
        self.object_list = self.filter_queryset(queryset)
        queryset =  self.object_list
        serializer = PropertySerializer(queryset, many=True)
        return Response(serializer.data)

class addProperty(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def create(self, request, *args, **kwargs):
        super(addProperty, self).create(request, args, kwargs)
        return Response({"message": "Success"})

class DetailProperty(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
