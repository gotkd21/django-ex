from django.shortcuts import render
from django.conf import settings

# Create your views here.
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):

    return render(request, 'weather_tracker/index.html')
