from rest_framework import mixins, generics, permissions
from app.usuario.models.usuario import Usuario
from app.usuario.api.serializers import UsuariosSerializer


class UsuariosSerializerView(generics.ListAPIView):
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Usuario.objects.all()


