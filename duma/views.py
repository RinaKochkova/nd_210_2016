from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def factions(request):
    template = loader.get_template('factions.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def deputies(request):
    template = loader.get_template('deputies.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


# Create your views here.
