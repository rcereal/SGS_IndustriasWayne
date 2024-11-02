from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recurso(models.Model):
    nome = models.CharField(max_length=100)
    descricao =  models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ])
    criado_em = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.nome