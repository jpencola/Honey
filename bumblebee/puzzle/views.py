from django.shortcuts import render_to_response
from django.template import RequestContext

from bumblebee.puzzle.models import Puzzle

def show_puzzle(request, guid="DEFAULT"):
    puzzle = Puzzle.objects.select_related().get(guid = guid)
    response_data = {"puzzle":{
                         "name": puzzle.name,
                         "width": puzzle.width,
                         "height": puzzle.height,
                         "max_rows": puzzle.difficulty.grid.rows,
                         "max_cols": puzzle.difficulty.grid.columns
                         }
                     }
    return render_to_response("puzzle.html",
                              response_data,
                              mimetype="text/html",
                              context_instance=RequestContext(request))
    