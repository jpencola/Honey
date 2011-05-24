from random import randint
from time import gmtime, strftime
import base64

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.files import File

from bumblebee.website.forms import UploadFileForm
from bumblebee.puzzle.models import ImageUpload, Puzzle, Difficulty, ImageDetail

def play_puzzle(request):
    pass

def create_puzzle(request):
    """ """
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        guid = create_guid()
         
        # create a Difficulty object based on form value
        req_difficulty = request.POST['difficulty']
        difficulty = Difficulty.objects.get(value = req_difficulty)
        
        # create the image from the upload
        file = request.FILES['file']
        image = create_image(file)
        
        # construct the new puzzle object
        req_puzzle_name =  request.POST['name']
        puzzle = Puzzle.objects.create(
                        guid = guid,
                        name = req_puzzle_name,
                        height = 400,
                        width = 400,
                        difficulty = difficulty
                        )
        
        ImageDetail.objects.create(
                       file = image, 
                       aviary_url = "http://www.jpencola.com",
                       puzzle = puzzle
                       )
        
        # display the completed puzzle on a page
        return HttpResponseRedirect('/puzzles/%s') % (guid)
    else:
        form = UploadFileForm()
        
    return render_to_response("create-puzzle.html",
                              {'form': form},
                              mimetype="text/html",
                              context_instance=RequestContext(request))
    
    
def create_guid():
    """ create a GUID using Base64 hash """
    rand = randint(100, 999)
    time = strftime("%H:%M:%S", gmtime())
    combined = "%s,%s" % (time, rand)
    guid = base64.b64encode(combined) 
    return guid


def create_image(file):
    """ """
    image = ImageUpload()
    f = File(file)
    image.file.save(file.name, f, save=False)
    image.save()
    return image
