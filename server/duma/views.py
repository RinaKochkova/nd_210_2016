from django.http import HttpResponse
from django.template import loader

from .models import *


def mainpage(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def factions_index(request):
    template = loader.get_template('factions.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def factions_details(request, id):
    template = loader.get_template('deputies.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def deputy_details(request, id):
    template = loader.get_template('deputies.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def stats(request):
    template = loader.get_template('deputies.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


# Create your views here.
