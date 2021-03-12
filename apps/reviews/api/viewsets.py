from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from ..models import Review
from .serializers import ReviewSerializer
import datetime

class GetReviews(viewsets.ViewSet):
    def list(self, request):
        queryset = Review.objects.all().order_by('feedback')
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

class addReview(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        super(addReview, self).create(request, args, kwargs)
        return Response({"message": "Success"})

class DetailReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
