from django.urls import path
from . import views
from .api.viewsets import GetCities, addCity, DetailCity


urlpatterns = [
    path('cities', GetCities.as_view({'get': 'list'}), name=None),
    path('cities/add', addCity.as_view(), name=None),
    path('cities/<int:pk>', DetailCity.as_view(), name=None),
]
