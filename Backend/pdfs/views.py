from django.views import View
from django.http import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .utils import compress_pdf
import os
from django.conf import settings

# FOLDER = str(os.getenv('DOWNLOADED_FOLDER'))
FILE_DIR = os.path.join(settings.BASE_DIR,os.environ.get('DOWNLOADED_FOLDER','Downloads'))
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class CompressorView(View):

    def post(self,request: request.HttpRequest):
        try:
            if 'file' in request.FILES:
                filename = request.FILES['file']
                file = request.FILES['file'].read()
                if file:
                    output_file = os.path.join(FILE_DIR,f'compressed-{filename}')
                    input_file = os.path.join(FILE_DIR,f'{filename}')
                    with open(input_file,'wb') as writer:
                        writer.write(file)
                    compress_pdf(input_file,output_file)
                    os.remove("demofile.txt")
            return JsonResponse({"success": True}, status=200)
        except Exception as e:
            return JsonResponse({'success':False},status=400)
        

                 