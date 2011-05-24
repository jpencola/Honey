from django.shortcuts import render_to_response
from django.template import RequestContext

from bumblebee.puzzle.models import Puzzle

def show_puzzle(request, guid="DEFAULT"):
    puzzle = Puzzle.objects.get(guid__exact=guid)
    response_data = {puzzle: puzzle}
    return render_to_response("puzzle.html",
                              response_data,
                              mimetype="text/html",
                              context_instance=RequestContext(request))
    