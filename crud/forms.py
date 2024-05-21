from django import forms
from .models import *

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['titulo', 'status']