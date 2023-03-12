from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    celular = models.CharField(max_length=11)
    endereco = models.CharField(max_length=150)
    nivel = models.CharField(max_length=1)
    nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    n_registro_cnh = models.CharField(max_length=11, blank=True, null=True)
    cdi = models.CharField(max_length=12, blank=True, null=True)
    assinatura_digital = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nome.title()}'
    
    class Meta:
        db_table = 'usuario'
        