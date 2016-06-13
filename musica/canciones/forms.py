#encondin:utf-8
from django.forms import ModelForm
from django import forms
from .models import canciones
from albums.models import albums
from artistas.models import artistas

class cancionesForm(forms.ModelForm):
	id_album = forms.ModelChoiceField(queryset=albums.objects.all())
	id_artista = forms.ModelChoiceField(queryset=artistas.objects.all())
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'error','placeholder':'Ingrece el nombre de la cancion'}))

	class Meta:
		model = canciones
		fields= ['id_album', 'id_artista', 'nombre']