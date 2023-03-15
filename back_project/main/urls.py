"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from django.urls import path, include, re_path

from django.views.generic import TemplateView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls'))
	]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

"""
"""
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from app.empresa.api import viewsets as empresaviewsets

from app.usuario.api import viewsets as usuariosviewset
from app.usuario.api import viewsets as usuarioviewset

from app.chat_usuario.api import viewsets as perguntasviewset
from app.chat_usuario.api import viewsets as perguntaviewset

from app.chat_usuario.api import viewsets as respostasviewset
from app.chat_usuario.api import viewsets as respostaviewset


router = routers.DefaultRouter()

route_empresa = routers.DefaultRouter()
route_empresa.register(r'', empresaviewsets.EmpresaViewset, basename='empresas')

route_usuarios = routers.DefaultRouter()
route_usuarios.register(r'', usuariosviewset.UsuariosViewset, basename='usuarios')

route_perguntas = routers.DefaultRouter()
route_perguntas.register(r'', perguntasviewset.PerguntasViewset, basename='perguntas')

route_respostas = routers.DefaultRouter()
route_respostas.register(r'', respostasviewset.RespostasViewset, basename='respostas')
"""

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('empresas/', include(route_empresa.urls)),
    path('usuarios/', include(route_usuarios.urls)),
    path('usuario/<int:id>/', usuarioviewset.UsuarioViewset.as_view(), name='usuario'),
    path('usuario/', usuarioviewset.UsuarioViewset.as_view(), name='usuario'),
    path('perguntas/', include(route_perguntas.urls)),
    path('pergunta/<int:id>/', perguntaviewset.PerguntaViewset.as_view(), name='pergunta'),
    path('pergunta/', perguntaviewset.PerguntaViewset.as_view(), name='pergunta'),
    path('respostas/', include(route_respostas.urls)),
    path('resposta/<int:id>/', respostaviewset.RespostaViewset.as_view(), name='resposta'),
    path('resposta/', respostaviewset.RespostaViewset.as_view(), name='resposta'),
	path('api-auth/', include('rest_framework.urls'))
]"""

"""
urlpatterns = [
    path('usuarios/', usuariosviewset , name='UsuariosViewset')
]"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('usuarios/', include('usuarios.urls'))
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

