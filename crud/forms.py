from django import forms
from .models import *

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['titulo', 'status']

class PesquisaForm(forms.Form):
    query = forms.CharField(label='Pesquise uma tarefa...', max_length=80, required=False)