from django.conf.urls.defaults import patterns, url
from bumblebee.puzzle import views

urlpatterns = patterns('',
    url(r'^puzzle', views.show_puzzle, name='puzzle'),
)