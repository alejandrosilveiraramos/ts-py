from django.db import models
from django.utils import timezone

from empresa.models import Empresa

class Documentos(models.Model):
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=20)
    numero_documento = models.CharField(max_length=20)
    data_emissao = models.DateField()
    arquivo_documento = models.FileField(upload_to='documentos/')      # Necessário estipular o caminho do arquivo EX: models.FileField(upload_to='pdf/')
    data_upload_documento = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f'{self.tipo_documento} - {self.empresa_id.nome_fantasia}'
    
    class Meta:
        db_table = 'documentos'
    