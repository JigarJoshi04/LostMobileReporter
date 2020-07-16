from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ReportModel(models.Model):
    imei_number= models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=150)
    mobile_company = models.CharField(max_length=100)
    mobile_model = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
