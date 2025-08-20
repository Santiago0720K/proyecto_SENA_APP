from django.urls import path
from . import views

app_name = 'aulas'

urlpatterns = [
    path('', views.lista_aulas, name='lista_aulas'),
    path('registrar/', views.registrar_aula, name='registrar_aula'),
]