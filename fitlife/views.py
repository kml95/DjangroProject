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

def calculator_view(request):
    if request.method == "POST":
        is_counted = True
        weight = int(request.POST['waga'])
        height = int(request.POST['wzrost'])
        wynik = (weight * height) / 2
        context = {
            'is_counted': is_counted,
            'wynik': wynik,
        }
        return render(request, 'fitlife/calculator.html', context)
    else:
        is_counted = False
        context = {
            'is_counted': is_counted,
        }
        return render(request, 'fitlife/calculator.html', context)
