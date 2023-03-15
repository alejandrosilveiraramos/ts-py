from rest_framework import viewsets
from app.empresa.api import serializers
from app.empresa.models.empresa import Empresa


class EmpresaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaSerializer
    queryset = Empresa.objects.all()
    




