from __future__ import unicode_literals

from django.db import models

from artistas.models import artistas

# Create your models here.

class albums(models.Model):
	id_album = models.AutoField(primary_key=True)
	id_artista = models.ForeignKey(artistas, null=True)
	nombreAl = models.CharField(max_length=40)
	genero = models.CharField(max_length=60)
    
def __str__(self):
  	return str(self.id_album)