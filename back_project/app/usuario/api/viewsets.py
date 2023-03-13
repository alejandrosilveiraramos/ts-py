from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from app.usuario.api import serializers
from app.usuario.models.usuario import Usuario

from rest_framework import status


class UsuariosViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UsuariosSerializer
    queryset = Usuario.objects.all()

  
class UsuarioViewset(APIView):
    
    def get(self, request, id):
        usuario = Usuario.objects.get(id=id)
        serializer = serializers.UsuariosSerializer(usuario)
        
        return Response(serializer.data)
    
    
    def put(self, request, id):
        usuario = Usuario.objects.get(id=id)
        serializer = serializers.UsuariosSerializer(usuario, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self, request):
        serializer = serializers.UsuariosSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id):
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    




