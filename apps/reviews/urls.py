from django.urls import path
from . import views
from .api.viewsets import GetReviews, addReview, DetailReview


urlpatterns = [
    path('reviews', GetReviews.as_view({'get': 'list'}), name=None),
    path('reviews/add', addReview.as_view(), name=None),
    path('reviews/<int:pk>', DetailReview.as_view(), name=None),
]
