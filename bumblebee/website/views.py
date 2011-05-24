import os
import imghdr
import string
import base64
from random import randint
from time import gmtime, strftime
from datetime import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.files import File

from bumblebee.puzzle.post_processing import process
from bumblebee.website.forms import UploadFileForm
from bumblebee.puzzle.models import ImageUpload, Puzzle, Difficulty, ImageDetail

ALLOWED_IMAGE_TYPES = ('png','jpg','jpeg',)
PUZZLE_SIZE = (400, 300,)

def create_puzzle(request):
    """ """
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        file = request.FILES['file']
        
        if request.META.has_key('X-Forwarded-For'):
            ip = request.META['X-Forwarded-For']
        else:
            ip = request.META['REMOTE_ADDR']
        
        guid = create_guid(ip)
         
        # First check the upload is a valid image file
        valid_image = matches_allowed_type(file)
        if valid_image:
            file_extension = os.path.splitext(file.name)[1]
            if file_extension == 'jpeg':    #normalize jpg|jpeg
                file_extension = 'jpg'
            day_id = datetime.now().day
            new_file_name = "%s_%s" % (day_id, ip)
            new_file_name = "%s%s" % (base64.b64encode(new_file_name, "AB"), file_extension)
            image = create_image(file, new_file_name)
            
            # Retrieve a Difficulty object based on the form's value
            difficulty = request.POST['difficulty']
            difficulty = Difficulty.objects.select_related().get(value = difficulty)
            filter = difficulty.filters.all()[0]
            
            # Send the new image file to Aviary for processing
            processed_image_url, image_url = process(image, file_extension, filter)
            
            req_puzzle_name = request.POST['name']
            puzzle = Puzzle.objects.create(
                            guid = guid,
                            name = req_puzzle_name,
                            width = PUZZLE_SIZE[0],
                            height = PUZZLE_SIZE[1],
                            difficulty = difficulty
                            )
            
            ImageDetail.objects.create(
                           file = image, 
                           aviary_url = image_url,
                           aviary_processed_url = processed_image_url,
                           puzzle = puzzle
                           )
            
            # display the new puzzle on a page
            return HttpResponseRedirect('/puzzles/%s' % (guid,))
        else:
            # show the error to the user
            return HttpResponseRedirect('/create_puzzle/errrr')
    else:
        form = UploadFileForm()
        
    return render_to_response("create-puzzle.html",
                              {'form': form},
                              mimetype="text/html",
                              context_instance=RequestContext(request))
    

def wrong_file_type(request):
    """ 
        When the user tries to upload a filetype that's 
        not supported, show them an error page
    """
    return render_to_response("error.html",
                              {},
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
    