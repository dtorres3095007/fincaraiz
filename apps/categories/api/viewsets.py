from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from ..models import Category
from .serializers import CategorySerializer
import datetime

class GetCategories(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all().order_by('slug')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class addCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        super(addCategory, self).create(request, args, kwargs)
        return Response({"message": "Success"})

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
