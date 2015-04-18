from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from django.template.loader import get_template

def index(request):
    return HttpResponse('<h3>index page</h3>')

def signup(request):
    tmplt = get_template('signup.html')
    html = tmplt.render(RequestContext(request, {'title': 'demo page'}))
    return HttpResponse(html)
