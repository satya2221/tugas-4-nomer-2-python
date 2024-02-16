from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template import loader

def halamanIndex(request):
    return render(request, "index.html")

def halamanPerkenalan(request):
    return render(request, 'perkenalan.html')
