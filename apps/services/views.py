from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.files.uploadedfile import TemporaryUploadedFile, InMemoryUploadedFile
from .uploaded_file import ChunkUploadedFile
from .utils import is_video
from tinymce.widgets import TinyMCE


def request_budget(request):
    if request.method == "GET":
        HTML_FIELD = TinyMCE().render(name='descricao', value='', attrs={'id': 'id_descricao'})
        return render(request, 'request_budget.html', {'HTML_FIELD': HTML_FIELD})
    elif request.method == "POST":
        file = request.FILES.get('file')
        if not is_video(file):
            raise HttpResponseBadRequest()
        
        file_upload = ChunkUploadedFile(file)
        file_upload.save_disk()
                            
        return HttpResponse('teste')