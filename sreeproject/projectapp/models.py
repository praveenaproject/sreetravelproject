from django.db import models


# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class Team(models.Model):
    name1 = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to='pic')
    desc1 = models.TextField()

    # def__str__(self):
    # return self.name
