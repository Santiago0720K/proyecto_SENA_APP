from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['nombre', 'codigo', 'nivel_formacion', 'duracion_meses', 'centro_formacion', 'modalidad', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del programa'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código'}),
            'nivel_formacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nivel de formación'}),
            'duracion_meses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duración en meses'}),
            'centro_formacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Centro de formación'}),
            'modalidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modalidad'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}),
        }
