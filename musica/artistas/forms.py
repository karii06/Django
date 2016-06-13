#encoding:utf-8
from django.forms import ModelForm
from django import forms 
from .models import artistas

class artistasForm(forms.ModelForm):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'error', 'placeholder':'Ingrese el nombre del artista'}))
	descrip = forms.CharField(widget=forms.Textarea(attrs={'class':'error', 'placeholder':'Ingrese una descipcion'}))

	class Meta:
		model = artistas
		fields =['nombre','descrip']