from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Log in error!')
    else:
        form = LoginForm()

    return render(request, 'loginuser/login.html', {'form':form})


def register_view(request):
    # if request.method == "POST":
    #     firstname = request.POST['firstname']
    #     lastname = request.POST['lastname']
    #     email = request.POST['email']
    #     username = request.POST['username']
    #     password = request.POST['password']

    #     User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
    #     return HttpResponseRedirect(reverse('home'))
    # else:
    #     return render(request, 'loginuser/register.html')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()
    
    return render(request, 'loginuser/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'home.html')