from django.shortcuts import render_to_response
from django.template import RequestContext
from apptortuguero.apps.registro.forms import addProductForm
from apptortuguero.apps.registro.models import Tortugas

def add_tortuga_view(request):
	if request.method == "POST":
		form = addProductForm(request.POST)
		info = "Inicializando"

		if form.is_valid():
			imagen			= form.cleaned_data['imagen']
			nombre 			= form.cleaned_data['nombre']
			especie 		= form.cleaned_data['especie']
			sexo 			= form.cleaned_data['sexo']
			sitioMonitoreo 	= form.cleaned_data['sitioMonitoreo']
			localizacion 	= form.cleaned_data['localizacion']
			longitud 		= form.cleaned_data['longitud']
			latitud 		= form.cleaned_data['latitud']
			marea 			= form.cleaned_data['marea']
			metodo 			= form.cleaned_data['metodo']
			placas 			= form.cleaned_data['placas']
			dernueva 		= form.cleaned_data['dernueva']
			izqnueva 		= form.cleaned_data['izqnueva']
			dervieja 		= form.cleaned_data['dervieja']
			izqvieja 		= form.cleaned_data['izqvieja']
			region 			= form.cleaned_data['region']

			LRC 			= form.cleaned_data['LRC']
			LCC 			= form.cleaned_data['LCC']
			ARC 			= form.cleaned_data['ARC']
			ACC 			= form.cleaned_data['ACC']
			LP 				= form.cleaned_data['LP']
			LTC 			= form.cleaned_data['LTC']
			PC 				= form.cleaned_data['PC']
			peso 			= form.cleaned_data['Peso']

			p = Tortugas()

			p.imagen = imagen
			p.nombre = nombre
			p.especie = especie
			p.sexo = sexo
			tiempo_reg = ""
			p.sitioMonitoreo = sitioMonitoreo
			p.localizacion = localizacion
			p.longitud = longitud
			p.latitud = latitud
			p.marea = marea
			p.metodo = metodo
			p.placas = placas
			p.dernueva = dernueva
			p.izqnueva = izqnueva
			p.dervieja = dervieja
			p.izqvieja = izqvieja
			p.region = region
			p.status = True

			p.LRC	= LRC 
			p.LCC	= LCC 
			p.ARC	= ARC 
			p.ACC	= ACC 
			p.LP	= LP 	
			p.LTC	= LTC 
			p.PC 	= PC 	
			p.peso  = peso

			p.save()
			info = "Se Guardo Satisfactoriamente"
		else:
			info = "Informacion con datos incorrectos"
			form = addProductForm()
			ctx = {'form':form, 'informacion':info}
			return render_to_response('agregando/addTortuga.html',ctx,context_instance = RequestContext(request))

	else:
		form = addProductForm()
		ctx = {'form':form}
    	return render_to_response('agregando/addTortuga.html',ctx,context_instance = RequestContext(request))