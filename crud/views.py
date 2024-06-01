from django.shortcuts import render, redirect, get_object_or_404
from .forms import ListaForm, PesquisaForm
from .models import Lista
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# view para visualizar a lista
@login_required
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

@login_required
def status(request, lista_id):
    try:
        lista = Lista.objects.get(id=lista_id, user=request.user)
        lista.status = not lista.status
        lista.save()
        return JsonResponse({'success': True, 'status': lista.status})
    except Lista.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'LISTA not found.'})
    
# view para deletar um item da lista

@login_required
def deletar(request, lista_id):
    try:
        lista = Lista.objects.get(id=lista_id, user=request.user)
        lista.delete()
        return JsonResponse({'success': True})
    except Lista.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'object not found.'})
    
# view para editar um item da lista

@login_required
def editar(request, lista_id):
    lista = get_object_or_404(Lista, id=lista_id, user=request.user)
    if request.method == 'POST':
        form = ListaForm(request.POST, instance=lista)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        return JsonResponse({'titulo': lista.titulo, 'status': lista.status})