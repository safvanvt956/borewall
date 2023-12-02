from django.db import models

# Create your models here.
   
class Project(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    dec = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Blog(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField()
    contact = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.FloatField()
    message = models.TextField()

    def __str__(self):
        return self.fullname

    