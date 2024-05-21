from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('todos/toggle-complete/<int:lista_id>/', status, name='todo_toggle_complete'),
]


