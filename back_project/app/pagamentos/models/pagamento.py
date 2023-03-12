from django.db import models
from django.core.validators import MinValueValidator

from app.empresa.models.solicitacao import Solicitacao

class Pagamento(models.Model):
    solicitacao_id = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=12, null=False, validators=[MinValueValidator(0.01)])
    forma_pagamento = models.CharField(max_length=50, null=False)
    data_pagamento = models.DateField(null=False)
    status_pagamento = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return f'{self.solicitacao_id} - {self.status_pagamento}'

    class Meta:
        db_table = 'pagamento'
        
        