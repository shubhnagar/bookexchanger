from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Books(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    contact = models.CharField(max_length=100)
    

    