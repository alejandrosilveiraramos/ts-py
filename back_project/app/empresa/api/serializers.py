from rest_framework import serializers
from app.empresa.models.empresa import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


