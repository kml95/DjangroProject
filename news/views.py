from django.template import RequestContext
from django.shortcuts import render

from news.models import *


def index(request):
    news = News.objects.all().order_by('-posted_date')
    return render(request, 'index.html', {'news': news})