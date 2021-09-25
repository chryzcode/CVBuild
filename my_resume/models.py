from django.db import models
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length= 25)
    location = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)
    occupation = models.TextField()
    summary = models.TextField()
    site = models.CharField(max_length=700, null=True, blank=True)
    twitter_url = models.CharField(max_length=250, null = True, blank = True)
    github_url = models.CharField(max_length=250, null = True, blank = True)
    linkedin_url = models.CharField(max_length=250, null = True, blank = True)
    dribble_url = models.CharField(max_length=250, null = True, blank = True)
    figma_url = models.CharField(max_length=250, null = True, blank = True)
    codepen_url = models.CharField(max_length=250, null = True, blank = True)
    behance_url = models.CharField(max_length=250, null = True, blank = True)

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.name

class Skills(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.name

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=200)
    post_held = models.CharField(max_length=30)
    year_from = models.DateField()
    year_to = models.DateField(null=True, blank=True)
    info = models.TextField()

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.company_name

class Education(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    school_name = models.CharField(max_length=30)
    school_location = models.CharField(max_length=150)
    degree = models.CharField(max_length=30)
    year_from = models.DateField()
    year_to = models.DateField(null=True, blank=True)
    info = models.TextField()

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.school_name

class Awards(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    award = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.award

class Project(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=40)
    source_code = models.CharField(max_length=150, null = True, blank = True)
    live = models.CharField(max_length=150, null = True, blank = True)
    info = models.TextField(max_length=200)

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.name

class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post_held = models.CharField(max_length=30)
    organization = models.CharField(max_length=100)
    year_from = models.DateField()
    year_to = models.DateField(null=True, blank=True)
    info = models.TextField()

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.post_held


