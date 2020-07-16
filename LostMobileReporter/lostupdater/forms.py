from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class ReportForm(forms.Form):
    class Meta:
        model = models.ReportModel
        fields= ['imei_number','mobile_number',
        'mobile_company','mobile_model','email_id']


