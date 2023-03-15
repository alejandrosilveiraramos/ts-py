from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=150)
    expediente = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.nome.title()}'
    
    class Meta:
        db_table = 'contato'
        