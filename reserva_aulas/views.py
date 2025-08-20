from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Aula

def registrar_aula(request):

    if request.method == 'POST':
        # 1. Obtiene los datos del formulario enviado por POST
        numero_aula = request.POST.get('numeroAula')
        nombre_aula = request.POST.get('nombreAula')
        tipo_aula = request.POST.get('tipoAula')
        capacidad = request.POST.get('capacidad')
        sede = request.POST.get('sede')
        estado = request.POST.get('estado')
        descripcion = request.POST.get('descripcion')
        
        # 2. Maneja los equipos (checkboxes) como una lista
        equipos_list = request.POST.getlist('equipos')
        equipos = ", ".join(equipos_list) # Convierte la lista a un string separado por comas

        # 3. Crea una nueva instancia del modelo Aula
        try:
            aula_nueva = Aula.objects.create(
                numero_aula=numero_aula,
                nombre_aula=nombre_aula,
                tipo_aula=tipo_aula,
                capacidad=capacidad,
                sede=sede,
                estado=estado,
                equipamiento=equipos,
                descripcion=descripcion,
            )
            
            # 4. Agrega un mensaje de éxito para mostrar en la plantilla
            messages.success(request, f'¡Aula {aula_nueva.numero_aula} registrada exitosamente!')
            
            # 5. Redirige a la misma URL para evitar el reenvío del formulario
            return redirect('aulas:registrar_aula')
        except Exception as e:
            # En caso de error, muestra un mensaje de advertencia
            messages.warning(request, f'Ocurrió un error al registrar el aula: {e}')
            return redirect('aulas:registrar_aula')
            
    # Si la solicitud no es POST (es decir, es GET), solo renderiza el formulario
    return render(request, 'reserva_aulas/registrar_aula.html')

def lista_aulas(request):
    aulas = Aula.objects.all()
    context = {
        'aulas': aulas,
    }
    return render(request, 'reserva_aulas/lista_aulas.html', context)
