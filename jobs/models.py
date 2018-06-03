from django.db import models

class Job(models.Model):
    """ Description the Jobs model"""
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
