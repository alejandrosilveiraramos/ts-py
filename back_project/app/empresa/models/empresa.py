from django.db import models
from django.utils import timezone


class Empresa(models.Model):
    nome_fantasia = models.CharField(max_length=150)
    razao_social = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_fantasia
    
    class Meta:
        db_table = 'empresa'
        