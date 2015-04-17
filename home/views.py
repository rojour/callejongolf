from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from register.forms import PlayerForm, SponsorForm

def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))
    
def players(request):
    return render_to_response('home/player.html', context_instance=RequestContext(request))

def sponsors(request):
    return render_to_response('home/sponsor.html', context_instance=RequestContext(request))
    
def contactus(request):
    return render_to_response('home/contactus.html', context_instance=RequestContext(request))

def management(request):
    return render_to_response('home/management.html', context_instance=RequestContext(request))
