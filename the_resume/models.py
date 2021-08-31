from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    education = models.TextField(max_length=2000)
    skills = models.TextField(max_length=1000)
    experience = models.TextField(max_length=2000)
