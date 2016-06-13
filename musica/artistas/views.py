from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import artistas
from albums.models import albums
from .forms import artistasForm

def inicio(request):
    Artistas = artistas.objects.all()
    Albums = albums.objects.all()
    return render(request, 'inicio.html', {'Artistas': Artistas, 'Albums': Albums})

def artistasCreation(request, template='artistasForm.html'):
    form = artistasForm()
    if request.method == "POST":
        form = artistasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'artistasNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def artistasList(request):
    Artistas = artistas.objects.all()
    return render(request, 'artistasListado.html', {'Artistas': Artistas})

def artistasDetail(request, id_artista, template='artistasDetalle.html'):
    Artistas = get_object_or_404(artistas, pk=id_artista)
    return render_to_response(template, {'Artistas': Artistas}, context_instance=RequestContext(request))

def artistasDelete(request, id_artista):
    instance = get_object_or_404(artistas, id_artista=id_artista)
    instance.delete()
    Artistas = artistas.objects.all()
    return render(request, 'artistasListado.html', {'Artistas': Artistas})

def artistasUpdate(request, id_artista):
    instance = get_object_or_404(artistas, id_artista=id_artista)
    form = artistasForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Artistas = artistas.objects.all()
            return render(request, 'artistasListado.html', {'Artistas': Artistas})
    return render(request, 'artistasDetalle.html', {'form': form})
