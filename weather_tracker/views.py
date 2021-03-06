from django.shortcuts import render
from django.conf import settings
# from . import database
# from .models import Tracker Forecast

# from weather_tracker.forms import weatherdata
#from services import get_weatherdata
from .services import get_weatherdata
import time

cur_time = int(time.time())
cur_location = "42.19364,-87.96736"

from django.http import HttpResponse

# This is the new class created based on the direction on https://stackoverflow.com/questions/30259452/proper-way-to-consume-data-from-restful-api-in-django
# there are problems with the definition of the class.
# class WeatherPage(generic.Templateview):
def index(request):
    weather_data = get_weatherdata(cur_location,cur_time)
    return render(request, 'weather_tracker/index.html', {
        'wdata': weather_data
    })

# Create your views here.

# This was from the trials I attempted with forms.  Never got it to work.
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

# This is the original static page view creation
# def index(request):
#    return render(request, 'weather_tracker/index.html')
