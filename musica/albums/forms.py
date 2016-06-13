#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import albums
from artistas.models import artistas

class albumsForm(forms.ModelForm):
	
	id_artista = forms.ModelChoiceField(queryset = artistas.objects.all())
	nombreAl = forms.CharField(widget=forms.TextInput(attrs={'class':'error','placeholder':'Ingrece el nombre del album'}))
	genero = forms.CharField(widget=forms.TextInput(attrs={'class':'error','placeholder':'Ingrece el genero del album'}))

	class Meta:
		model = albums
		fields = ['id_artista', 'nombreAl', 'genero']