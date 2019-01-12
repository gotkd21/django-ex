from django.db import models

# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

class Tracker(models.Model):
    timestamp = models.DateTimeField()
    curlattitude = models.DecimalField(max_digits=6, decimal_places=3)
    curlongtitude = models.DecimalField(max_digits=6, decimal_places=3)
    currentpressure = models.DecimalField(max_digits=6, decimal_places=2)
