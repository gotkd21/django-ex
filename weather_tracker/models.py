from django.db import models

# Create your models here.
class Tracker(models.Model):
    timestamp = models.DateTimeField()
    curlattitude = models.DecimalField(max_digits=6, decimal_places=3)
    curlongtitude = models.DecimalField(max_digits=6, decimal_places=3)
    currentpressure = models.DecimalField(max_digits=6, decimal_places=2)

class Forecast(models.Model):
    timestamp = models.DateTimeField()
    curlattitude = models.DecimalField(max_digits=6, decimal_places=3)
    curlongtitude = models.DecimalField(max_digits=6, decimal_places=3)
    currentpressure = models.DecimalField(max_digits=6, decimal_places=2)
