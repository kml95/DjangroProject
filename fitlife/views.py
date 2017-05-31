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

def calculatorBMI_view(request):
    if request.method == "POST":
        is_counted = True
        weight = float(request.POST['waga'])
        height = float(request.POST['wzrost'])
        wynik = weight/((height/100)*(height/100))
        context = {
            'is_counted': is_counted,
            'wynik': wynik,
        }
        return render(request, 'fitlife/calculatorBMI.html', context)
    else:
        is_counted = False
        context = {
            'is_counted': is_counted,
        }
        return render(request, 'fitlife/calculatorBMI.html', context)

def calculatorBMR_view(request):
    if request.method == "POST":
        if request.POST.get("count_again"):
            return render(request, 'fitlife/calculatorBMR.html')
        else:      
            is_counted = True
            sex = request.POST['sex']
            age = int(request.POST['age'])
            weight = int(request.POST['weight'])
            height = int(request.POST['height'])
            if sex == "male":
                result = (10*weight)+(6*height)-(5*age)+5
            else:
                result = (10*weight)+(6*height)-(5*age)-161
            context = {
                'is_counted': is_counted,
                'result': result,
            }
            return render(request, 'fitlife/calculatorBMR.html', context)
    else:
        is_counted = False
        context = {
            'is_counted': is_counted,
        }
    return render(request, 'fitlife/calculatorBMR.html', context)

def calculatorWeight_view(request):
    if request.method == "POST":
        if request.POST.get("count_again"):
            return render(request, 'fitlife/calculatorWeight.html')
        else:      
            is_counted = True
            sex = request.POST['sex']
            height = int(request.POST['height'])
            minimalna = float(height/100)*float(height/100)*18.5
            maksymalna = float(height/100)*float(height/100)*25
            if sex == "male":
                Broca = (height-100)*0.9
                Pottona = height-100-(height-100)/20
                Lorentza = height-100-0.25*(height-150)
            else:
                Broca = (height-100)*0.85
                Pottona = height-100-(height-100)/10
                Lorentza = height-100-0.5*(height-150)
            context = {
                'minimalna': minimalna,
                'maksymalna': maksymalna,
                'is_counted': is_counted,
                'Broca': Broca,
                'Pottona': Pottona,
                'Lorentza': Lorentza,
            }
            return render(request, 'fitlife/calculatorWeight.html', context)
    else:
        is_counted = False
        context = {
            'is_counted': is_counted,
        }
    return render(request, 'fitlife/calculatorWeight.html', context)