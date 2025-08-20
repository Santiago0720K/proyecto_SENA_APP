# SENA_APP/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URLs con prefijos únicos para cada aplicación
    path('admin/', admin.site.urls),
    path('', include('aprendices.urls')),  # 'inicio' debe estar en aprendices/urls.py
    path('aulas/', include('reserva_aulas.urls')),
    path('instructores/', include('instructores.urls')),
    path('programas/', include('programas.urls')),
]

# Personalización del panel administrativo
admin.site.site_header = "Panel Administrativo SENA"
admin.site.site_title = "SENA APP"
admin.site.index_title = "Gestión de Aprendices"