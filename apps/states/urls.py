from django.urls import path
from . import views
from .api.viewsets import GetStates, addState, DetailState


urlpatterns = [
    path('states', GetStates.as_view({'get': 'list'}), name=None),
    path('states/add', addState.as_view(), name=None),
    path('states/<int:pk>', DetailState.as_view(), name=None),
]
