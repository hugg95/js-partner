from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
import os.path

# Create your views here.

def hello(request):
    return HttpResponse(os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'))

def demo(request):
    t = get_template('demo.html')
    html = t.render(Context({'title': 'demo page'}))
    return HttpResponse(html)