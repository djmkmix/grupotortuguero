from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('apptortuguero.apps.registro.views',
	url(r'^add/tortuga/$','add_tortuga_view', name='vista_agregar_tortuga'),

)