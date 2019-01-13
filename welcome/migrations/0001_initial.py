# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('hostname', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('anothername', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('timestamp', models.DateTimeField()),
                ('curlattitude', models.DecimalField(max_digits=6, decimal_places=3)),
                ('curlongtitude', models.DecimalField(max_digits=6, decimal_places=3)),
                ('currentpressure', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
    ]
