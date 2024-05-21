from django.shortcuts import render
from .forms import ListaForm
from .models import Lista


def index(request):
    lista = Lista.objects.filter(usuario=request.user)
    return render(request, 'index.html', {'lista': lista})