from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.files import File

from bumblebee.website.forms import UploadFileForm
from bumblebee.puzzle.models import ImageUpload

def create_puzzle(request):
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        file = request.FILES['file']
        image = create_image(file)
        
        # display the completed puzzle on a page
        return HttpResponseRedirect('/puzzle/234kldjf23453')
    else:
        form = UploadFileForm()
        
    return render_to_response("create-puzzle.html",
                              {'form': form},
                              mimetype="text/html",
                              context_instance=RequestContext(request))# Create your views here.


def create_image(file):
    """"""
    image = ImageUpload()
    f = File(file)
    image.file.save(file.name, f, save=False)
    image.save()
    
    return image


def upload_image(request):
    """"""
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        file = request.FILES['file']
        image = create_image(file)
        
        return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
        
    return render_to_response('create-puzzle.html', {'form': form})
