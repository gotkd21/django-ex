# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-21 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_tracker', '0002_auto_20190121_0450'),
    ]

    operations = [
        migrations.CreateModel(
            name='wforecast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('curlattitude', models.DecimalField(decimal_places=3, max_digits=6)),
                ('curlongtitude', models.DecimalField(decimal_places=3, max_digits=6)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('summary', models.CharField(max_length=30, null=True)),
                ('icon', models.CharField(choices=[('CD', 'clear-day'), ('CN', 'clear-night'), ('RN', 'rain'), ('SN', 'snow'), ('SL', 'sleet'), ('WI', 'wind'), ('CL', 'cloudy'), ('PD', 'partly-cloudy-day'), ('PN', 'partly-cloudy-night'), ('HL', 'hail'), ('TH', 'thunderstorm'), ('TR', 'tornado')], max_length=2, null=True)),
                ('precipIntensity', models.DecimalField(decimal_places=4, max_digits=6, null=True)),
                ('precipProbability', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('precipAccumulation', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('precipType', models.CharField(max_length=10, null=True)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('apparentTemperature', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('dewPoint', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('uvIndex', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('visibility', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('ozone', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='wtracker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('curlattitude', models.DecimalField(decimal_places=3, max_digits=6)),
                ('curlongtitude', models.DecimalField(decimal_places=3, max_digits=6)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('summary', models.CharField(max_length=30, null=True)),
                ('icon', models.CharField(choices=[('CD', 'clear-day'), ('CN', 'clear-night'), ('RN', 'rain'), ('SN', 'snow'), ('SL', 'sleet'), ('WI', 'wind'), ('CL', 'cloudy'), ('PD', 'partly-cloudy-day'), ('PN', 'partly-cloudy-night'), ('HL', 'hail'), ('TH', 'thunderstorm'), ('TR', 'tornado')], max_length=2, null=True)),
                ('precipIntensity', models.DecimalField(decimal_places=4, max_digits=6, null=True)),
                ('precipProbability', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('precipAccumulation', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('precipType', models.CharField(max_length=10, null=True)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('apparentTemperature', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('dewPoint', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('uvIndex', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('visibility', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('ozone', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.DeleteModel(
            name='Forecast',
        ),
        migrations.DeleteModel(
            name='Tracker',
        ),
    ]
