from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index(request):
    return render_to_response('index.html', None)


def run(request):
    pass


def save(request):
    pass


# user signup
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']

        if password == password_confirm:
            user = User.objects.create_user(name, email, password)
            user.save()
            return HttpResponseRedirect('/')

    return render_to_response('user/signup.html', RequestContext(request))


# user login
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        print name
        print password
        # remember = request.POST.get('remember', False)
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')

    return render_to_response('user/login.html', RequestContext(request))


# user change password
def change_password(request):
    if request.method != 'POST':
        return render_to_response('user/change_password.html')