from django.db import models
from django.utils import timezone


class Operador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    senha = models.CharField(max_length=64)
    perfil = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome.title()}'
    
    class Meta:
        db_table = 'operador'
        