from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from ..models import Transaction
from .serializers import TransactionSerializer
import datetime

class GetTransactions(viewsets.ViewSet):
    def list(self, request):
        queryset = Transaction.objects.all().order_by('slug')
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

class addTransaction(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        super(addTransaction, self).create(request, args, kwargs)
        return Response({"message": "Success"})

class DetailTransaction(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
