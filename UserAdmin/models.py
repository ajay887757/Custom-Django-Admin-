from django.db import models

# Create your models here.


class Cloud(models.Model):
    name = models.CharField(max_length=108)
    Address = models.TextField()

    def __str__(self):
        return self.name



class restaurants(models.Model):
    name = models.CharField(max_length=108)
    Address = models.TextField()
    distance=models.IntegerField(null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True)

    def __str__(self) :
        return self.name
