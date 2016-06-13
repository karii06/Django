from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import albums
from canciones.models import canciones 
from artistas.models import artistas
from .forms import albumsForm

def inicio(request):
    Artistas = artistas.objects.all()
    Albums = albums.objects.all()
    Aanciones = canciones.objects.all()
    return render(request, 'inicio.html', {'Artistas': Artistas, 'Albums': Albums, 'Aanciones':Aanciones})

def albumsCreation(request, template='albumsForm.html'):
    form = albumsForm()
    if request.method == "POST":
        form = albumsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'albumsNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def albumsList(request):
    Albums = albums.objects.all()
    return render(request, 'albumsListado.html', {'Albums': Albums})

def albumsDetail(request, id_album, template='albumsDetalle.html'):
    Albums = get_object_or_404(albums, pk=id_album)
    return render_to_response(template, {'Albums': Albums}, context_instance=RequestContext(request))

def albumsDelete(request, id_album):
    instance = get_object_or_404(albums, id_album=id_album)
    instance.delete()
    Albums = albums.objects.all()
    return render(request, 'albumsListado.html', {'Albums': Albums})

def albumsUpdate(request, id_album):
    instance = get_object_or_404(albums, id_album=id_album)
    form = albumsForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Albums = albums.objects.all()
            return render(request, 'albumsListado.html', {'Albums': Albums})
    return render(request, 'albumsDetalle.html', {'form': form})
