from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import Exercise, Products,Types


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

def films_view(request):    
    return render(request, 'fitlife/films.html')

def trainingplan_view(request):
    if request.method == "POST":
        if request.POST.get("count_again"):
            return render(request, 'fitlife/trainingplan.html')
        else:      
            is_counted = True
            trainingvalue = 0
            sex = request.POST['sex']
            if sex == "male":
                target = request.POST['target']
                if target == "strength":
                    trainingvalue = 1
                else:
                    trainingvalue = 2
            else:
                target = request.POST['target']
                if target == "strength":
                    trainingvalue = 3
                else:
                    trainingvalue = 4

            context = {
                'is_counted': is_counted,
                'trainingvalue': trainingvalue,
            }
            return render(request, 'fitlife/trainingplan.html', context)
    else:
        return render(request, 'fitlife/trainingplan.html')

def calculators_view(request):
    return render(request, 'fitlife/calculators.html')

<<<<<<< Updated upstream
def products_view(request):
    if request.method == "POST":
        if request.POST.get("back"):
            types=Types.objects.all()
            context = { 'types':types }
            return render(request, 'fitlife/products.html', context)
        else:
            type = request.POST['type']
            typeo = Types.objects.get(typical=type)
            products=Products.objects.filter(typical=typeo)
            context = { 'products':products,'type':type }
            return render(request, 'fitlife/products.html', context)
    
    else:
        types=Types.objects.all()
        context = { 'types':types }
        return render(request, 'fitlife/products.html', context)
=======
def dietplan_view(request):
    if request.method == "POST":
        if request.POST.get("count_again"):
            return render(request, 'fitlife/dietplan.html')
        else:      
            is_counted = True
            dietValue = 0
            target = request.POST['target']
            activity = request.POST['activity']
            weight = int(request.POST['weight'])
            if target == "mass":
                if activity == "low":
                    kcal = weight*25*1.2+300
                    carbo = kcal/8
                    protein = kcal/16
                    fat = kcal/36
                    carbopermeal = carbo/5
                    proteinpermeal = protein/5
                    fatpermeal = fat/5

                    dietValue = 1
                elif activity == "medium":
                    kcal = weight*25*1.5+300
                    carbo = kcal/8
                    protein = kcal/16
                    fat = kcal/36
                    carbopermeal = carbo/5
                    proteinpermeal = protein/5
                    fatpermeal = fat/5

                    dietValue = 2
                else:
                    kcal = weight*25*1.7+300
                    carbo = kcal/8
                    protein = kcal/16
                    fat = kcal/36
                    carbopermeal = carbo/5
                    proteinpermeal = protein/5
                    fatpermeal = fat/5

                    dietValue = 3
            else:
                if activity == "low":
                    kcal = weight*25*1.2-300
                    carbo = kcal/8
                    protein = kcal/16
                    fat = kcal/36
                    carbopermeal = carbo/5
                    proteinpermeal = protein/5
                    fatpermeal = fat/5

                    dietValue = 4
                elif activity == "medium":
                    kcal = weight*25*1.5-300
                    carbo = kcal/8
                    protein = kcal/16
                    fat = kcal/36
                    carbopermeal = carbo/5
                    proteinpermeal = protein/5
                    fatpermeal = fat/5

                    dietValue = 5
                else:
                    kcal = weight*25*1.7-300
                    carbo = kcal/8
                    protein = kcal/16
                    fat = kcal/36
                    carbopermeal = carbo/5
                    proteinpermeal = protein/5
                    fatpermeal = fat/5

                    dietValue = 6

            context = {
                'is_counted': is_counted,
                'dietValue': dietValue,
                'kcal': kcal,
                'carbo': carbo,
                'protein': protein,
                'fat': fat,
                'carbopermeal': carbopermeal,
                'proteinpermeal': proteinpermeal,
                'fatpermeal': fatpermeal,
            }
            return render(request, 'fitlife/dietplan.html', context)
    else:
        return render(request, 'fitlife/dietplan.html')
>>>>>>> Stashed changes
