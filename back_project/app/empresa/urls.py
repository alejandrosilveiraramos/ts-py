from django.urls import path

from app.empresa.views import empresa, index


urlpatterns = [
    path('', index.index, name='index'),
    path('empresa', empresa.empresa, name='empresa'),
    # path('', views.index, name='index'),
    # path('empresa', views.empresa, name='empresa'),
]       

