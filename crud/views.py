from django.shortcuts import render, redirect
from .forms import ListaForm
from .models import Lista


# view para visualizar a lista (READ)
def index(request):
    lista = Lista.objects.filter(user=request.user)
    form = ListaForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            lista = form.save(commit=False)
            lista.user = request.user
            lista.save()
            return redirect('index')
    else:
        form = ListaForm()
    return render(request, 'index.html', {'lista': lista, 'form': form})

# def criar_lista(request):
#     if request.method == 'POST':
#         form = ListaForm(request.POST)
#         if form.is_valid():
#             lista = form.save(commit=False)
#             lista.usuario = request.user
#             lista.save()
#             return redirect('index')
#     else:
#         form = ListaForm()
#     return render(request, 'criar_lista.html', {'form': form})