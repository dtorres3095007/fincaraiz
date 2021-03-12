from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from ..models import State
from .serializers import StateSerializer
import datetime

class GetStates(viewsets.ViewSet):
    def list(self, request):
        queryset = State.objects.all().order_by('slug')
        serializer = StateSerializer(queryset, many=True)
        return Response(serializer.data)

class addState(generics.CreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def create(self, request, *args, **kwargs):
        super(addState, self).create(request, args, kwargs)
        return Response({"message": "Success"})

class DetailState(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
