from django.urls import path
from . import views
from .api.viewsets import GetProperties, addProperty, DetailProperty


urlpatterns = [
    path('properties', GetProperties.as_view(), name=None),
    path('properties/add', addProperty.as_view(), name=None),
    path('properties/<int:pk>', DetailProperty.as_view(), name=None),
]
