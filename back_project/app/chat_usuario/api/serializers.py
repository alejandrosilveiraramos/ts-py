from rest_framework import serializers

from app.chat_usuario.models.perguntas import Perguntas
from app.chat_usuario.models.respostas import Respostas
        

class PerguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perguntas
        fields = '__all__'


class RespostasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respostas
        fields = '__all__'
