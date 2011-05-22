from django.shortcuts import render_to_response
from django.template import RequestContext

#from bumblebee import settings

def create_puzzle(request):
    response_data = {}
    return render_to_response("create-puzzle.html",
                              response_data,
                              mimetype="text/html",
                              context_instance=RequestContext(request))# Create your views here.
