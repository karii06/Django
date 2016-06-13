from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from albums.models import albums
from artistas.models import artistas
from .models import canciones
from .forms import cancionesForm


def inicio(request):
    Artistas = artistas.objects.all()
    Albums = albums.objects.all()
    Canciones = canciones.objects.all()
    return render(request, 'inicio.html', {'Artistas': Artistas, 'Albums': Albums, 'Canciones':Canciones})

def cancionesCreation(request, template='cancionesForm.html'):
    form = cancionesForm()
    if request.method == "POST":
        form = cancionesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'cancionesNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def cancionesList(request):
    Canciones = canciones.objects.all()
    return render(request, 'cancionesListado.html', {'Canciones': Canciones})

def cancionesDetail(request, id_cancion, template='cancionesDetalle.html'):
    Canciones = get_object_or_404(canciones, pk=id_cancion)
    return render_to_response(template, {'Canciones': Canciones}, context_instance=RequestContext(request))

def cancionesDelete(request, id_cancion):
    instance = get_object_or_404(canciones, id_cancion=id_cancion)
    instance.delete()
    Canciones = canciones.objects.all()
    return render(request, 'cancionesListado.html', {'Canciones': Canciones})

def cancionesUpdate(request, id_cancion):
    instance = get_object_or_404(canciones, id_cancion=id_cancion)
    form = cancionesForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Canciones = canciones.objects.all()
            return render(request, 'cancionesListado.html', {'Canciones': Canciones})
    return render(request, 'cancionesDetalle.html', {'form': form})
