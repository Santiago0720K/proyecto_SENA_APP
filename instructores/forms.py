from django import forms
from .models import Instructor

class InstructorForm(forms.Form):
    tipo_documento = forms.ChoiceField(
        choices=Instructor.TIPO_DOCUMENTO_CHOICES, 
        label="Tipo de Documento",
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )
    
    documento_identidad = forms.CharField(
        max_length=20, 
        label="Documento de Identidad",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el número de documento'
        })
    )
    
    nombre = forms.CharField(
        max_length=100, 
        label="Nombre",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre'
        })
    )
    
    apellido = forms.CharField(
        max_length=100, 
        label="Apellido",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el apellido'
        })
    )
    
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    telefono = forms.CharField(
        max_length=10, 
        required=False, 
        label="Teléfono",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el teléfono'
        })
    )
    
    correo = forms.EmailField(
        required=False, 
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@correo.com'
        })
    )
    
    ciudad = forms.CharField(
        max_length=100, 
        required=False, 
        label="Ciudad",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese la ciudad'
        })
    )
    
    direccion = forms.CharField(
        required=False, 
        label="Dirección",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese la dirección completa',
            'rows': 3
        })
    )
    
    nivel_educativo = forms.ChoiceField(
        choices=Instructor.NIVEL_EDUCATIVO_CHOICES, 
        label="Nivel Educativo",
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )
    
    especialidad = forms.CharField(
        max_length=100, 
        label="Especialidad",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese la especialidad'
        })
    )
    
    anos_experiencia = forms.IntegerField(
        min_value=0, 
        label="Años de Experiencia",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '0',
            'min': '0'
        })
    )
    
    activo = forms.BooleanField(
        required=False, 
        initial=True, 
        label="Activo",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    
    fecha_vinculacion = forms.DateField(
        label="Fecha de Vinculación",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    fecha_registro = forms.DateField(
        label="Fecha de Registro",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        documento = cleaned_data.get('documento_identidad')
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')

        if not documento or not nombre or not apellido:
            raise forms.ValidationError("Todos los campos obligatorios deben ser completados.")

        return cleaned_data

    def clean_documento_identidad(self):
        documento = self.cleaned_data['documento_identidad']
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento
        
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono
        
    def save(self):
        """Método para guardar el instructor en la base de datos"""
        try:
            instructor = Instructor.objects.create(
                documento_identidad=self.cleaned_data['documento_identidad'],
                tipo_documento=self.cleaned_data['tipo_documento'],
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
                telefono=self.cleaned_data.get('telefono', ''),
                correo=self.cleaned_data.get('correo', ''),
                fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
                ciudad=self.cleaned_data.get('ciudad', ''),
                direccion=self.cleaned_data.get('direccion', ''),
                nivel_educativo=self.cleaned_data['nivel_educativo'],
                especialidad=self.cleaned_data['especialidad'],
                anos_experiencia=self.cleaned_data['anos_experiencia'],
                activo=self.cleaned_data.get('activo', True),
                fecha_vinculacion=self.cleaned_data['fecha_vinculacion'],
                fecha_registro=self.cleaned_data['fecha_registro']
            )
            return instructor
        except Exception as e:
            raise forms.ValidationError(f"Error al crear el instructor: {str(e)}")