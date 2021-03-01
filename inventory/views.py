from django.shortcuts import render
from .models import Part

def index(request):
    parts = Part.objects.all()
    return render(request, 'index.html', {'parts': parts})
