from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from django import forms


def index(request):
    return HttpResponse('<h3>index page</h3>')

def signup(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render_to_response('signup.html')