from django.shortcuts import render
from django.conf import settings
# from . import database
# from .models import Tracker Forecast

# from weather_tracker.forms import weatherdata
#from services import get_weatherdata
#import time

# Create your views here.
from django.http import HttpResponse

#def get_data(request):
#        get_data.wlocation = "42.19364,-87.96736"
#        get_data.wtime = int(time.time())
#        form = init_request_form(request.get)
#        return render(request, 'name.html', {'form': form})


# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

#    return render(request, 'welcome/index.html', {
#        'hostname': hostname,
#        'database': database.info(),
#        'count': PageView.objects.count()
#    })

def index(request):
    return render(request, 'weather_tracker/index.html')
