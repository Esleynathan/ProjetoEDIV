from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.files.uploadedfile import TemporaryUploadedFile, InMemoryUploadedFile
from .uploaded_file import ChunkUploadedFile
from .utils import is_video


def request_budget(request):
    if request.method == "GET":
        return render(request, 'request_budget.html')
    elif request.method == "POST":
        file = request.FILES.get('file')
        if not is_video(file):
            raise HttpResponseBadRequest()
        
        file_upload = ChunkUploadedFile(file)
        file_upload.save_disk()
                            
        return HttpResponse('teste')