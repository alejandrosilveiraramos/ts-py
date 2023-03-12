from django.urls import path

from app.pagamentos.views import pagamento


urlpatterns = [
    path('pagamento', pagamento.pagamento, name='pagamento'),
]       

