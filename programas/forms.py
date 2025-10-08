from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['nombre', 'codigo', 'nivel_formacion', 'duracion_meses', 'centro_formacion', 'modalidad', 'descripcion']
        labels = {
            'nombre': 'Nombre del Programa',
            'codigo': 'Código del Programa',
            'nivel_formacion': 'Nivel de Formación',
            'duracion_meses': 'Duración (meses)',
            'centro_formacion': 'Centro de Formación',
            'modalidad': 'Modalidad',
            'descripcion': 'Descripción del Programa'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Técnico en Desarrollo de Software'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el código del programa'
            }),
            'nivel_formacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Técnico, Tecnólogo, Especialización'
            }),
            'duracion_meses': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '1'
            }),
            'centro_formacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del centro de formación'
            }),
            'modalidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Presencial, Virtual, Mixta'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese una descripción breve del programa (opcional)',
                'rows': 4
            }),
        }
    
    def clean_duracion_meses(self):
        duracion = self.cleaned_data.get('duracion_meses')
        if duracion and duracion < 1:
            raise forms.ValidationError("La duración debe ser al menos de 1 mes.")
        return duracion
    
    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if codigo:
            codigo = codigo.strip().upper()
        return codigo