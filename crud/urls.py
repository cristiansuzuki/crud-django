from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('/nova-lista/', criar_lista, name='criar-lista'),
]