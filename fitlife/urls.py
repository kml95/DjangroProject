from django.conf.urls import url

from . import views

app_name = 'fitlife'
urlpatterns = [
    url('^training/$', views.training_view, name='training'),
    url('^calculatorBMI/$', views.calculatorBMI_view, name='calculatorBMI'),
    url('^calculatorBMR/$', views.calculatorBMR_view, name='calculatorBMR'),
    url('^calculatorWeight/$', views.calculatorWeight_view, name='calculatorWeight'),
]