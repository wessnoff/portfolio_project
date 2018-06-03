from django.db import models

# Create your models here.
class Blog(models.Model):
    """Blog model"""
    title = models.CharField(max_length=60)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    img = models.ImageField(upload_to='images/blog/')
    body = models.TextField(null=True)
