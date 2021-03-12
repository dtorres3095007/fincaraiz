from django.urls import path
from . import views
from .api.viewsets import GetTransactions, addTransaction, DetailTransaction


urlpatterns = [
    path('transactions', GetTransactions.as_view({'get': 'list'}), name=None),
    path('transactions/add', addTransaction.as_view(), name=None),
    path('transactions/<int:pk>', DetailTransaction.as_view(), name=None),
]
