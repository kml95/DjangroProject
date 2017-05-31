from django.shortcuts import get_object_or_404, render

from news.views import index

def home_view(request):
    #return render(request, 'home.html')
    return index(request)