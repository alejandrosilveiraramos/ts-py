from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from app.chat_usuario.api import serializers
from app.chat_usuario.models.perguntas import Perguntas
from app.chat_usuario.models.respostas import Respostas

from rest_framework import status


class PerguntasViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PerguntasSerializer
    queryset = Perguntas.objects.all()


class PerguntaViewset(APIView):
    
    def get(self, request, id):
        pergunta = Perguntas.objects.get(id=id)
        serializer = serializers.PerguntasSerializer(pergunta)
        
        return Response(serializer.data)
    
    
    def put(self, request, id):
        pergunta = Perguntas.objects.get(id=id)
        serializer = serializers.PerguntasSerializer(pergunta, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self, request):
        serializer = serializers.PerguntasSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id):
        pergunta = Perguntas.objects.get(id=id)
        pergunta.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


  
class RespostasViewset(viewsets.ModelViewSet):
    serializer_class = serializers.RespostasSerializer
    queryset = Respostas.objects.all()


class RespostaViewset(APIView):
    
    def get(self, request, id):
        resposta = Respostas.objects.get(id=id)
        serializer = serializers.RespostasSerializer(resposta)
        
        return Response(serializer.data)
    
    
    def put(self, request, id):
        resposta = Respostas.objects.get(id=id)
        serializer = serializers.RespostasSerializer(resposta, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self, request):
        serializer = serializers.RespostasSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id):
        resposta = Respostas.objects.get(id=id)
        resposta.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    




