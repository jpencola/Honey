from django.shortcuts import render_to_response
from django.template import RequestContext

from bumblebee.puzzle.models import Puzzle

def http_fourhundredfour_error(request):
    return render_to_response("404.html",
                              {},
                              mimetype="text/html",
                              context_instance=RequestContext(request))
    
def http_fivehundred_error(request):
    return render_to_response("500.html",
                              {},
                              mimetype="text/html",
                              context_instance=RequestContext(request))

def show_puzzle(request, guid="DEFAULT"):
    puzzle = Puzzle.objects.select_related().get(guid = guid)
    first_associated_image = puzzle.imagedetail_set.all()[0]
    response_data = {"puzzle":{
                         "name": puzzle.name,
                         "width": puzzle.width,
                         "height": puzzle.height,
                         "difficulty_name": puzzle.difficulty.name,
                         "max_rows": puzzle.difficulty.grid.rows,
                         "max_cols": puzzle.difficulty.grid.columns,
                         "source_url": first_associated_image.aviary_url,
                         "processed_url": first_associated_image.aviary_processed_url,
                         }
                     }
    return render_to_response("puzzle.html",
                              response_data,
                              mimetype="text/html",
                              context_instance=RequestContext(request))
    