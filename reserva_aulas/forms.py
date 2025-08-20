from django import forms
from .models import Aula

class AulaForm(forms.ModelForm):
    # Opciones para los equipos (checkboxes)
    EQUIPOS_CHOICES = [
        ('proyector', 'Proyector'),
        ('computador', 'Computador'),
        ('parlantes', 'Parlantes'),
        ('microfono', 'Micrófono'),
        ('pizarra_digital', 'Pizarra Digital'),
        ('pizarra_acrilica', 'Pizarra Acrílica'),
        ('aire_acondicionado', 'Aire Acondicionado'),
        ('wifi', 'WiFi'),
        ('television', 'Televisión'),
        ('mesa_profesor', 'Mesa de Profesor'),
        ('sillas_estudiantes', 'Sillas para Estudiantes'),
        ('escritorios', 'Escritorios'),
    ]
    
    # Campo para equipos como MultipleChoiceField
    equipos = forms.MultipleChoiceField(
        choices=EQUIPOS_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        }),
        required=False,
        label="Equipos Disponibles"
    )

    class Meta:
        model = Aula
        fields = [
            'numero_aula', 
            'nombre_aula', 
            'tipo_aula', 
            'capacidad', 
            'sede', 
            'estado', 
            'descripcion'
        ]
        
        widgets = {
            'numero_aula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: A-101, Lab-205',
                'required': True
            }),
            'nombre_aula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre descriptivo del aula'
            }),
            'tipo_aula': forms.Select(attrs={
                'class': 'form-control'
            }),
            'capacidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '200',
                'placeholder': 'Número de personas'
            }),
            'sede': forms.Select(attrs={
                'class': 'form-control'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción adicional del aula...'
            }),
        }
        
        labels = {
            'numero_aula': 'Número de Aula',
            'nombre_aula': 'Nombre del Aula',
            'tipo_aula': 'Tipo de Aula',
            'capacidad': 'Capacidad',
            'sede': 'Sede/Localización',
            'estado': 'Estado',
            'descripcion': 'Descripción Adicional',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Si estamos editando un aula existente, pre-seleccionar los equipos
        if self.instance.pk and self.instance.equipamiento:
            equipos_actuales = [equipo.strip() for equipo in self.instance.equipamiento.split(',')]
            self.fields['equipos'].initial = equipos_actuales

    def clean_numero_aula(self):
        """Validación personalizada para el número de aula"""
        numero_aula = self.cleaned_data.get('numero_aula')
        
        if numero_aula:
            # Convertir a mayúsculas para consistencia
            numero_aula = numero_aula.upper().strip()
            
            # Verificar que no esté vacío después del strip
            if not numero_aula:
                raise forms.ValidationError("El número de aula no puede estar vacío.")
                
        return numero_aula

    def clean_capacidad(self):
        """Validación personalizada para la capacidad"""
        capacidad = self.cleaned_data.get('capacidad')
        
        if capacidad is not None:
            if capacidad < 1:
                raise forms.ValidationError("La capacidad debe ser mayor a 0.")
            if capacidad > 500:
                raise forms.ValidationError("La capacidad no puede ser mayor a 500.")
                
        return capacidad

    def save(self, commit=True):
        """Sobrescribir el método save para manejar los equipos"""
        instance = super().save(commit=False)
        
        # Convertir la lista de equipos en un string separado por comas
        equipos_seleccionados = self.cleaned_data.get('equipos', [])
        instance.equipamiento = ', '.join(equipos_seleccionados)
        
        if commit:
            instance.save()
            
        return instance