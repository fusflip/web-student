from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    template = loader.get_template('wiki-1-glavn.html')
    return HttpResponse(template.render({},request))

def login(request):
    template = loader.get_template('wiki-1-vhod.html')
    return HttpResponse(template.render({},request))
	
def profil(request):
    template = loader.get_template('wiki-1-profil.html')
    return HttpResponse(template.render({},request))
	
def discipline(request):
    template = loader.get_template('wiki-1-discipl.html')
    return HttpResponse(template.render({},request))

def discipline_change(request):
    template = loader.get_template('wiki-1-discipl_red.html')
    return HttpResponse(template.render({},request))

def registration(request):
    template = loader.get_template('wiki-1-registr.html')
    return HttpResponse(template.render({},request))