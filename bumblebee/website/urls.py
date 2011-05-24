from django.conf.urls.defaults import patterns, url
from bumblebee.website import views

urlpatterns = patterns('',
    url(r'^errrr/', views.wrong_file_type, name='error'),
    url(r'^$', views.create_puzzle, name='create_puzzle'),
)