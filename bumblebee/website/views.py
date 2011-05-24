import os
import imghdr
import string
import base64
from random import randint
from time import gmtime, strftime

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.files import File

from bumblebee.website.forms import UploadFileForm
from bumblebee.puzzle.models import ImageUpload, Puzzle, Difficulty, ImageDetail

ALLOWED_IMAGE_TYPES = ('png','jpg','jpeg','gif','tif',)

def create_puzzle(request):
    """ """
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        
        if request.META.has_key('X-Forwarded-For'):
            ip = request.META['X-Forwarded-For']
        else:
            ip = request.META['REMOTE_ADDR']
                
        guid = create_guid(ip)
         
        # create a Difficulty object based on form value
        req_difficulty = request.POST['difficulty']
        difficulty = Difficulty.objects.get(value = req_difficulty)
        
        # First check the upload is a valid image file
        file = request.FILES['file']
        valid_image = matches_allowed_type(file)
        if valid_image:
            file_extension = os.path.splitext(file.name)[1]
            
            new_file_name = ip + file_extension
            image = create_image(file, new_file_name)
            
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
            
            # display the new puzzle on a page
            return HttpResponseRedirect('/puzzles/'+guid )
        else:
            # show the error to the user
            return HttpResponseRedirect('/invalid_image/')
    else:
        form = UploadFileForm()
        
    return render_to_response("create-puzzle.html",
                              {'form': form},
                              mimetype="text/html",
                              context_instance=RequestContext(request))
    
    
def create_guid(ip):
    """ create a GUID using Base64 hash algo """
    rand_str = str(randint(100, 999))
    time = strftime("%H:%M:%S", gmtime())
    combined = ' '.join((ip, time, rand_str,))
    guid = base64.b64encode(string.strip(combined), 'AB') 
    return guid


def create_image(file, name):
    """ create the new image file and save it """
    image = ImageUpload()
    f = File(file)
    image.file.save(name, f, save=False)
    image.save()
    return image


def matches_allowed_type(file):
    """ check that the image type matches an allowed type """
    image_type = imghdr.what(file.name, file.read())
    if image_type in ALLOWED_IMAGE_TYPES:
        return True
    else:
        return False