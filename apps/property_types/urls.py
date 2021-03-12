from django.urls import path
from . import views
from .api.viewsets import GetPropertyTypes, addPropertyType, DetailPropertyType


urlpatterns = [
    path('property_types', GetPropertyTypes.as_view({'get': 'list'}), name=None),
    path('property_types/add', addPropertyType.as_view(), name=None),
    path('property_types/<int:pk>', DetailPropertyType.as_view(), name=None),
]
