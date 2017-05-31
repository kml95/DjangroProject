from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .forms import LoginForm, RegisterForm
import random, string
from .models import UserConfirmation
from .email_sender import send_confirmation_email

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                confirm=UserConfirmation.objects.get(user=user)
                if confirm.confirmed == False:
                    return HttpResponse('Account is not activated')
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Log in error!')
    else:
        form = LoginForm()

    return render(request, 'loginuser/login.html', {'form':form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            random_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
            user=User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
            UserConfirmation.objects.create(user=user,confirmed=False,code=random_code)
            send_confirmation_email(receiver=user,confirmation_code=random_code)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()
    
    return render(request, 'loginuser/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'home.html')

def confirm_view(request,username,code):
    user=User.objects.get(username=username)
    confirm=UserConfirmation.objects.get(user=user)
    if code==confirm.code:
        confirm.confirmed=True
        confirm.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        raise Http404

