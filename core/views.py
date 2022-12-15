from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    from pathlib import Path
    BASE_DIR = Path(__file__).resolve().parent.parent
    content = f'{BASE_DIR}'
    return HttpResponse(content)