from django.shortcuts import render, redirect
from .forms import ListaForm, PesquisaForm
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


# lógica para filtrar pelo campo de pesquisa
    form_pesquisa = PesquisaForm(request.GET or None)
    query = request.GET.get('query')
    if query:
        lista = Lista.objects.filter(user=request.user, titulo__icontains=query)
    else:
        lista = Lista.objects.filter(user=request.user)

    return render(request, 'index.html', {'lista': lista, 'form': form, 'form_pesquisa': form_pesquisa})

# view para alterar status da lista
def status(request, lista_id):
    try:
        lista = Lista.objects.get(id=lista_id, user=request.user)
        lista.status = not lista.status
        lista.save()
        return JsonResponse({'success': True, 'status': lista.status})
    except Lista.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'LISTA not found.'})
    
# view para deletar um item da lista
def deletar(request, lista_id):
    try:
        lista = Lista.objects.get(id=lista_id, user=request.user)
        lista.delete()
        return JsonResponse({'success': True})
    except Lista.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'object not found.'})
