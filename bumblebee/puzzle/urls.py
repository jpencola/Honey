from django.conf.urls.defaults import patterns, url
from bumblebee.puzzle import views

urlpatterns = patterns('',
    url(r'(?P<guid>[a-zA-Z0-9_=.-]+)/$', views.show_puzzle, name='puzzle'),
    url(r'(?P<guid>[a-zA-Z0-9_=.-]+)$', views.show_puzzle, name='puzzle'),
    url(r'^', views.show_puzzle, name='puzzle'),
)