from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Exercise

def training_view(request):
    if request.method == "POST":
        is_generated = True
        exercises = Exercise.objects.all()
        context = {
            'is_generated': is_generated,
            'exercises': exercises,
        }
        return render(request, 'fitlife/training.html', context)
    else:
        is_generated = False
        context = {
            'is_generated': is_generated,
        }
        return render(request, 'fitlife/training.html', context)
