from django.conf.urls.defaults import patterns, url
from bumblebee.puzzle import views

handler404 = 'views.http_fourhundredfour_error'
handler500 = 'views.http_fivehundred_error'

urlpatterns = patterns('',
    url(r'(?P<guid>[a-zA-Z0-9_=.-]+)/$', views.show_puzzle, name='puzzle'),
    url(r'(?P<guid>[a-zA-Z0-9_=.-]+)$', views.show_puzzle, name='puzzle'),
    url(r'^', views.show_puzzle, name='puzzle'),
)