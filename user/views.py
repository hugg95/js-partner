from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from user import models
import os.path

# Create your views here.

def test(request):
    return HttpResponse(os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'))

def signup(request):
    t = get_template('signup.html')
    html = t.render(RequestContext(request, {'title': 'demo page'}))
    return HttpResponse(html)

def user_signup(request):
    u = models.User.objects.create_user('victor')
    #u.save()
