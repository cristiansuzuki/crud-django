from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('todos/toggle-complete/<int:lista_id>/', status, name='todo_toggle_complete'),
    path('todos/delete/<int:lista_id>/', deletar, name='todo_delete'),
    path('editar/<int:lista_id>/', editar, name='editar'),
]


