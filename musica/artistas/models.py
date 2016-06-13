from __future__ import unicode_literals

from django.db import models

# Create your models here.

class artistas(models.Model):
	id_artista = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=40)
	descrip = models.CharField(max_length=200)

	def __unicode__(self):
		return str(self.id_artista)
