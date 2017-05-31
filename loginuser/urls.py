from django.conf.urls import url

from . import views

app_name = 'loginuser'
urlpatterns = [
    url('^login/$', views.login_view, name='login'),
    url('^register/$', views.register_view, name='register'),
    url('^logout/$', views.logout_view, name='logout'),
    url('^register/(?P<username>[A-Za-z0-9]+)/(?P<code>[A-Z0-9]{16,})/$', views.confirm_view,name='confirm' )
]