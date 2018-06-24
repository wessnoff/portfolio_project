from django.db import models


# Create your models here.
class Blog(models.Model):
    """Blog model"""
    title = models.CharField(max_length=60)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    img = models.ImageField(upload_to='images/blog/')
    body = models.TextField(null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y %X')
