from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

	#-->Mostrar pagina principal
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'artistas.views.inicio', name='inicio'),
    #-->Listar las tablas
    url(r'^artistas/listado/$','artistas.views.artistasList' , name='artistas_listado'),
    url(r'^canciones/listado/$','canciones.views.cancionesList' , name='canciones_listado'),
    url(r'^albums/listado/$','albums.views.albumsList' , name='albums_listado'),
    #-->Poblar tablas
    url(r'^artistas/nuevo/$','artistas.views.artistasCreation', name='artistas_nuevo'),
    url(r'^canciones/nuevo/$','canciones.views.cancionesCreation', name='canciones_nuevo'),
    url(r'^albums/nuevo/$','albums.views.albumsCreation', name='albums_nuevo'),
    #-->Editar tablas
    url(r'^artistas/(?P<id_artista>\d+)$','artistas.views.artistasUpdate', name='artistas_detalle'),
    url(r'^albums/(?P<id_album>\d+)$','albums.views.albumsUpdate', name='albums_detalle'),
    url(r'^canciones/(?P<id_cancion>\d+)$','canciones.views.cancionesUpdate', name='cancion_detalle'),
    #-->Eliminar registros
    url(r'^artistas_e/(?P<id_artista>\d+)$','artistas.views.artistasDelete', name='artistas_borrar'),
    url(r'^albums_e/(?P<id_album>\d+)$','albums.views.albumsDelete', name='albums_borrar'),
    url(r'^canciones_e/(?P<id_cancion>\d+)$','canciones.views.cancionesDelete', name='canciones_borrar'),
)