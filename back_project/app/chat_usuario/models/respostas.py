from django.db import models


class Respostas(models.Model):
    resposta_1 = models.CharField(max_length=150)
    resposta_2 = models.CharField(max_length=150)
    resposta_3 = models.CharField(max_length=150)
    resposta_4 = models.CharField(max_length=150)
    resposta_5 = models.CharField(max_length=150)
    resposta_6 = models.CharField(max_length=150)
    
    def __str__(self):
        return f'Respostas ao usuário'
    
    class Meta:
        db_table = 'respostas'
    