from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.empresa.urls')),
    path('usuario/', include('app.usuario.urls')),
    path('operador/', include('app.operador.urls')),
    path('empresa/', include('app.empresa.urls')),
    path('pagamento/', include('app.pagamentos.urls'))
]
