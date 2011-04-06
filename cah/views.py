from django.http import HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render

def index(request):
    if request.user.is_authenticated():
        template_name = "index_signedin.html"
    else:
        template_name = "index_signedout.html"
    return render(request, template_name, {})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')