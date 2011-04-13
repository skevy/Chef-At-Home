from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from cah.accounts.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.template.context import RequestContext

def index(request):
    pass

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                                email=form.cleaned_data['email_address'],
                                                password=form.cleaned_data['password1'])
            first_name, last_name = form.cleaned_data['full_name'].split(" ")
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            return redirect("signup_success")
    else:
        form = UserCreationForm()
        
    return render_to_response(
        'accounts/signup.html',
        { 'form': form },
        context_instance=RequestContext(request)
    )

def signup_success(request):
    return render(request, 'accounts/signup_success.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = AuthenticationForm()

    return render_to_response(
        'accounts/signin.html',
        { 'form': form },
        context_instance=RequestContext(request)
    )

def signout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')