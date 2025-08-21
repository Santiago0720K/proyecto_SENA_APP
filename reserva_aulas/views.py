from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Aula
from .forms import AulaForm

def registrar_aula(request):
    """Vista para registrar una nueva aula usando el formulario Django"""
    
    if request.method == 'POST':
        form = AulaForm(request.POST)
        
        if form.is_valid():
            try:
                aula_nueva = form.save()
                messages.success(request, f'¡Aula {aula_nueva.numero_aula} registrada exitosamente!')
                return redirect('aulas:lista_aulas')
            except Exception as e:
                messages.error(request, f'Ocurrió un error al registrar el aula: {e}')
        else:
            # El formulario tiene errores - se mostrarán automáticamente en el template
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = AulaForm()
    
    context = {
        'form': form
    }
    return render(request, 'reserva_aulas/registrar_aula.html', context)

def lista_aulas(request):
    """Vista para mostrar la lista de todas las aulas"""
    aulas = Aula.objects.all()
    context = {
        'aulas': aulas,
    }
    return render(request, 'reserva_aulas/lista_aulas.html', context)

def editar_aula(request, aula_id):
    """Vista para editar una aula existente"""
    aula = get_object_or_404(Aula, id=aula_id)
    
    if request.method == 'POST':
        form = AulaForm(request.POST, instance=aula)
        
        if form.is_valid():
            try:
                aula_actualizada = form.save()
                messages.success(request, f'¡Aula {aula_actualizada.numero_aula} actualizada exitosamente!')
                return redirect('aulas:lista_aulas')
            except Exception as e:
                messages.error(request, f'Ocurrió un error al actualizar el aula: {e}')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = AulaForm(instance=aula)
    
    context = {
        'form': form,
        'aula': aula,
        'editando': True
    }
    return render(request, 'reserva_aulas/registrar_aula.html', context)

def eliminar_aula(request, aula_id):
    """Vista para eliminar una aula directamente"""
    aula = get_object_or_404(Aula, id=aula_id)
    
    # Guardamos el número del aula antes de eliminarla
    numero_aula = aula.numero_aula
    
    try:
        aula.delete()
        messages.success(request, f'Aula {numero_aula} eliminada exitosamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar el aula: {e}')
    
    # Siempre redirigir a la lista de aulas
    return redirect('aulas:lista_aulas')