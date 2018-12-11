from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('wiki-1-glavn.html')
    return HttpResponse(template.render({},request))