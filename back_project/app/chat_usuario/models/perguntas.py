from django.db import models


class Perguntas(models.Model):
    pergunta_1 = models.CharField(max_length=150)
    pergunta_2 = models.CharField(max_length=150)
    pergunta_3 = models.CharField(max_length=150)
    pergunta_4 = models.CharField(max_length=150)
    pergunta_5 = models.CharField(max_length=150)
    pergunta_6 = models.CharField(max_length=150)
    
    def __str__(self):
        return f'Perguntas ao usuário'
    
    class Meta:
        db_table = 'perguntas'
    
        