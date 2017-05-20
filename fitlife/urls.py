from django.conf.urls import url

from . import views

app_name = 'fitlife'
urlpatterns = [
    url('^training/$', views.training_view, name='training'),
]