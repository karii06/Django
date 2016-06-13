from __future__ import unicode_literals

from django.db import models
from artistas.models import artistas
from albums.models import albums

# Create your models here.

class canciones(models.Model):
	id_cancion = models.AutoField(primary_key=True)
	id_album = models.ForeignKey(albums, null=True)
	id_artista = models.ForeignKey(artistas, null=True)
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return str(self.id_cancion)