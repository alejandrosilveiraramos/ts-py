from django.db import models
from django.utils import timezone

from app.empresa.models.empresa import Empresa
from app.usuario.models.usuario import Usuario

class Solicitacao(models.Model):
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pendente')
    data_solicitacao = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.status} - {self.empresa_id.nome_fantasia}'
    
    class Meta:
        db_table = 'solicitacao'
        