from django.urls import path


#from . import views

from app.usuario.views import usuario


urlpatterns = [
    path('usuario', usuario.usuario, name='usuario')
]       

