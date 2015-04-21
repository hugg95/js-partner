from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html', None)


def run(request):
    pass


def save(request):
    pass