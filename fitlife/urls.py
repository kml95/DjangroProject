from django.conf.urls import url

from . import views

app_name = 'fitlife'
urlpatterns = [
    url('^training/$', views.training_view, name='training'),
    url('^calculatorBMI/$', views.calculatorBMI_view, name='calculatorBMI'),
    url('^calculatorBMR/$', views.calculatorBMR_view, name='calculatorBMR'),
    url('^calculatorWeight/$', views.calculatorWeight_view, name='calculatorWeight'),
<<<<<<< Updated upstream
    url('^films/$', views.films_view, name='films'),
    url('^calculators/$', views.calculators_view, name='calculators'),
    url('^trainingplan/$', views.trainingplan_view, name='trainingplan'),
=======
    url ('^products/$', views.products_view, name='products')
>>>>>>> Stashed changes
]