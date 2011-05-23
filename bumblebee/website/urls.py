from django.conf.urls.defaults import patterns, url
from bumblebee.website import views

urlpatterns = patterns('',
    url(r'^$', views.create_puzzle, name='create_puzzle'),
    url(r'^puzzles/$', views.play_puzzle, name='play_puzzle'),
)