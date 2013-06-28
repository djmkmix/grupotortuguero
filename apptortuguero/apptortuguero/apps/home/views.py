from django.shortcuts import render_to_response
from django.template import RequestContext
from apptortuguero.apps.registro.models import Responsable,Tortugas

from apptortuguero.apps.home.forms import ContactForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage

def index_view(request):
    tortugas = Tortugas.objects.filter(status=True)

    ctx = {'tortugas':tortugas}
    return render_to_response('home/index.html',ctx,context_instance = RequestContext(request))


def tortugas_view(request):
    tortugas = Tortugas.objects.filter(status=True)

    ctx = {'tortugas':tortugas}
    return render_to_response('home/tortugas.html',ctx,context_instance = RequestContext(request))

def tortuga_view(request,id_local):
    local = Tortugas.objects.get(id=id_local)
    ctx = {'local' :local}
    return render_to_response('home/singleTortuga.html',ctx,context_instance=RequestContext(request))

def contacto_view(request):
    if request.method=='POST':
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            titulo = formulario.cleaned_data['Asunto']
            contenido = formulario.cleaned_data['Texto'] + "\n" + "\n"
            contenido +='Comunicarse a: ' + formulario.cleaned_data['Email'] + "\n" + "\n"
            contenido +='Con: ' + formulario.cleaned_data['Nombre']
            correo = EmailMessage(titulo,contenido, to=['agencia_puntoycoma@hotmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
        formulario = ContactForm()
    return render_to_response('home/contacto.html',{'form':formulario},context_instance = RequestContext(request))