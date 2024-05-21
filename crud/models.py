from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Lista(models.Model):
    titulo = models.CharField(max_length=80)
    status = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo