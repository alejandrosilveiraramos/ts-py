from django.urls import path

#from . import views

from app.operador.views import login, autenticar, logout, operador


urlpatterns = [
    path('operador', operador.operador, name='operador'),
    path('login', login.login, name='login'),
    path('autenticar/', autenticar.autenticar, name='autenticar'),
    path('logout/', logout.logout, name='logout')
]       

