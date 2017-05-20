from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Log in error!')
    else:
        return render(request, 'loginuser/login.html')

def register_view(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'loginuser/register.html')

def logout_view(request):
    logout(request)
    return render(request, 'home.html')