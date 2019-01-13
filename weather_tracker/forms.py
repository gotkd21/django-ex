# forms.py

from django import forms

class get_weatherdata(forms.Form):
    wlocation = forms.CharField(label='Enter Location: ', max_length=24)
    wtime = forms.DateTimeField(label='Enter Start Time', max_length=12)
