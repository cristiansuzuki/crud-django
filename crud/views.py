from django.shortcuts import render, redirect
from .forms import ListaForm
from .models import Lista
from django.http import JsonResponse

# view para visualizar a lista (READ)
def index(request):
    lista = Lista.objects.filter(user=request.user)
    form = ListaForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            lista = form.save(commit=False)
            lista.user = request.user
            lista.save()
            return JsonResponse({'success': True})
    else:
        form = ListaForm()
    return render(request, 'index.html', {'lista': lista, 'form': form})

def status(request, lista_id):
    try:
        lista = Lista.objects.get(id=lista_id, user=request.user)
        lista.status = not lista.status
        lista.save()
        return JsonResponse({'success': True, 'status': lista.status})
    except Lista.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'LISTA not found.'})
