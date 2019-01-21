from django.db import models


# Create your models here.

class WeatherInfo(models.Model):
    ICON_TEXT = (
        ('CD', 'clear-day'),
        ('CN', 'clear-night'),
        ('RN', 'rain'),
        ('SN', 'snow'),
        ('SL', 'sleet'),
        ('WI', 'wind'),
        ('CL', 'cloudy'),
        ('PD', 'partly-cloudy-day'),
        ('PN', 'partly-cloudy-night'),
        ('HL', 'hail'),
        ('TH', 'thunderstorm'),
        ('TR', 'tornado')
    )

    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    curlattitude = models.DecimalField(max_digits=6, decimal_places=3)
    curlongtitude = models.DecimalField(max_digits=6, decimal_places=3)
    pressure = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    summary = models.CharField(max_length=30,null=True)
    icon = models.CharField(max_length=2,null=True, choices=ICON_TEXT)
    precipIntensity = models.DecimalField(max_digits=6,decimal_places=4,null=True)
    precipProbability = models.DecimalField(max_digits=5, decimal_places=3,null=True)
    precipAccumulation = models.DecimalField(max_digits=5, decimal_places=3,null=True)
    precipType  = models.CharField(max_length=10,null=True)
    temperature = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    apparentTemperature = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    dewPoint = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    humidity = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    uvIndex = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    visibility = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    ozone = models.DecimalField(max_digits=6,decimal_places=2,null=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['timestamp'])
        ]

class wtracker(WeatherInfo):
    class Meta:
        ordering = ['timestamp']


class wforecast(WeatherInfo):
    class Meta:
        ordering = ['timestamp']


#class Tracker(models.Model):
#    id = models.AutoField(primary_key=True)
#    timestamp = models.DateTimeField()
#    curlattitude = models.DecimalField(max_digits=6, decimal_places=3)
#    curlongtitude = models.DecimalField(max_digits=6, decimal_places=3)
#    actual_pressure = models.DecimalField(max_digits=6, decimal_places=2)
#    actual_summary = models.CharField(max_length=30)
#    actual_icon = models.CharField(max_length=25)
#    actual_precipIntensity = models.DecimalField(max_digits=6,decimal_places=4)
#    actual_precipProbability = models.DecimalField(max_digits=5, decimal_places=3)
#    actual_precipAccumulation = models.DecimalField(max_digits=5, decimal_places=3)
#    actual_precipType  = models.CharField(max_length=10)
#    actual_temperature = models.DecimalField(max_digits=5,decimal_places=2)
#    actual_apparentTemperature = models.DecimalField(max_digits=5,decimal_places=2)
#    actual_dewPoint = models.DecimalField(max_digits=5,decimal_places=2)
#    actual_humidity = models.DecimalField(max_digits=5,decimal_places=2)
#    actual_uvIndex = models.DecimalField(max_digits=4,decimal_places=2)
#    actual_visibility = models.DecimalField(max_digits=5,decimal_places=2)
#    actual_ozone = models.DecimalField(max_digits=6,decimal_places=2)

#class Forecast(models.Model):
#    id = models.AutoField(primary_key=True)
#    timestamp = models.DateTimeField()
#    curlattitude = models.DecimalField(max_digits=6, decimal_places=3)
#    curlongtitude = models.DecimalField(max_digits=6, decimal_places=3)
#    fcast_pressure = models.DecimalField(max_digits=6, decimal_places=2)
#    fcast_summary = models.CharField(max_length=30)
#    fcast_icon = models.CharField(max_length=25)
#    fcast_precipIntensity = models.DecimalField(max_digits=6,decimal_places=4)
#    fcast_precipProbability = models.DecimalField(max_digits=5, decimal_places=3)
#    fcast_precipAccumulation = models.DecimalField(max_digits=5, decimal_places=3)
#    fcast_precipType  = models.CharField(max_length=10)
#    fcast_temperature = models.DecimalField(max_digits=5,decimal_places=2)
#    fcast_apparentTemperature = models.DecimalField(max_digits=5,decimal_places=2)
#    fcast_dewPoint = models.DecimalField(max_digits=5,decimal_places=2)
#    fcast_humidity = models.DecimalField(max_digits=5,decimal_places=2)
#    fcast_uvIndex = models.DecimalField(max_digits=4,decimal_places=2)
#    fcast_visibility = models.DecimalField(max_digits=5,decimal_places=2)
#    fcast_ozone = models.DecimalField(max_digits=6,decimal_places=2)
