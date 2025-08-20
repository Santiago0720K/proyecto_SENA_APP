from django.db import models

class Aula(models.Model): 
    # Opciones predefinidas para los campos de selección
    TIPO_AULA_CHOICES = [
        ('teorica', 'Aula Teórica'),
        ('laboratorio', 'Laboratorio'),
        ('taller', 'Taller'),
        ('auditorio', 'Auditorio'),
        ('sala_computo', 'Sala de Cómputo'),
        ('biblioteca', 'Biblioteca'),
        ('multiproposito', 'Multipropósito'),
    ]
    
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('mantenimiento', 'En Mantenimiento'),
        ('fuera_servicio', 'Fuera de Servicio'),
    ]
    
    SEDE_CHOICES = [
        ('sede_principal', 'Centro Minero'),
        ('sede_norte', 'CEDEAGRO'),
        ('sede_sur', 'CEGAFE'),
        ('sede_centro', 'Sede Sogamoso'),
    ]

    # Campos del modelo
    numero_aula = models.CharField(max_length=50, unique=True, verbose_name="Número de Aula")
    nombre_aula = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre del Aula")
    tipo_aula = models.CharField(max_length=20, choices=TIPO_AULA_CHOICES, verbose_name="Tipo de Aula")
    capacidad = models.IntegerField(verbose_name="Capacidad")
    sede = models.CharField(max_length=50, choices=SEDE_CHOICES, verbose_name="Localización")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible', verbose_name="Estado")
    equipamiento = models.CharField(max_length=255, blank=True, null=True, verbose_name="Equipos Disponibles")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción Adicional")

    # Campos de auditoría (opcional pero recomendado)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    def __str__(self):
        return f'{self.numero_aula} - {self.nombre_aula or "Sin Nombre"}'

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"
        ordering = ['numero_aula']

