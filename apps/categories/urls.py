from django.urls import path
from . import views
from .api.viewsets import GetCategories, addCategory, DetailCategory


urlpatterns = [
    path('categories', GetCategories.as_view({'get': 'list'}), name=None),
    path('categories/add', addCategory.as_view(), name=None),
    path('categories/<int:pk>', DetailCategory.as_view(), name=None),
]
