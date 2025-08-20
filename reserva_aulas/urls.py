from django.urls import path
from . import views

app_name = 'aulas'

urlpatterns = [
    # URL para registrar aula
    path('registrar/', views.registrar_aula, name='registrar_aula'),
    
    # URL para listar aulas
    path('lista/', views.lista_aulas, name='lista_aulas'),
    
    # URL para editar aula
    path('editar/<int:aula_id>/', views.editar_aula, name='editar_aula'),
    
    # URL para eliminar aula
    path('eliminar/<int:aula_id>/', views.eliminar_aula, name='eliminar_aula'),
    
    # URL raíz que redirecciona a la lista
    path('', views.lista_aulas, name='index'),
]