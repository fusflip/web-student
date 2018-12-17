from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required(login_url='/login')
def index(request):
    template = loader.get_template('wiki-1-glavn.html')
    return HttpResponse(template.render({},request))

def signIn(request):
    if request.POST:
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            uri = request.GET['next']
            return redirect(uri)
    template = loader.get_template('wiki-1-vhod.html')
    return HttpResponse(template.render({},request))
	
@login_required(login_url='/login')
def profil(request):
    template = loader.get_template('wiki-1-profil.html')
    return HttpResponse(template.render({},request))

@login_required(login_url='/login')
def discipline(request):
    template = loader.get_template('wiki-1-discipl.html')
    return HttpResponse(template.render({},request))

@login_required(login_url='/login')
def discipline_change(request):
    template = loader.get_template('wiki-1-discipl_red.html')
    return HttpResponse(template.render({},request))

def registration(request):
    template = loader.get_template('wiki-1-registr.html')
    return HttpResponse(template.render({},request))