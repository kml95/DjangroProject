from django.conf.urls import url

from . import views

app_name = 'fitlife'
urlpatterns = [
    url('^training/$', views.training_view, name='training'),
    url('^calculator/$', views.calculator_view, name='calculator')
]