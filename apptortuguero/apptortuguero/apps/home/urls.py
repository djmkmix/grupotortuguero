from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('apptortuguero.apps.home.views',
	url(r'^$','index_view', name='vista_principal'),
	url(r'^tortugas/$','tortugas_view', name='vista_tortugas'),
	url(r'^contacto/$','contacto_view', name='vista_contacto'),
	url(r'^tortuga/(?P<id_local>.*)/$','tortuga_view', name='vista_single_tortuga'),
)