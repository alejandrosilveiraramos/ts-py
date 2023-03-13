from rest_framework import serializers
from app.usuario.models.usuario import Usuario


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        


