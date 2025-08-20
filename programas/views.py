from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Programa
from .forms import ProgramaForm

# Lista de programas
def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('lista_programas.html')
    context = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))

# Detalle de programa
def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    cursos = programa.curso_set.all().order_by('-fecha_inicio')
    template = loader.get_template('detalle_programa.html')
    context = {
        'programa': programa,
        'cursos': cursos,
    }
    return HttpResponse(template.render(context, request))

# Crear programa
def crear_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Programa creado con éxito.')
            return redirect('programas:lista_programas')
    else:
        form = ProgramaForm()

    template = loader.get_template('crear_programa.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))