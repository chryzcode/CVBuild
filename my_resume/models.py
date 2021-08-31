from django.db import models
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length= 25)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=12)

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
    company_address = models.CharField(max_length=200)
    post_held = models.CharField(max_length=30)
    year_from = models.CharField(max_length=20)
    year_to = models.CharField(max_length=20)
    info = models.TextField()

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.company_name

class Education(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    school_name = models.CharField(max_length=30)
    school_address = models.CharField(max_length=150)
    degree = models.CharField(max_length=30)
    year_from = models.CharField(max_length=20)
    year_to = models.CharField(max_length=20)
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

class Languages(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    language = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.language

class Project(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=40)
    source_code = models.CharField(max_length=150, null = True, blank = True)
    live = models.CharField(max_length=150, null = True, blank = True)
    info = models.TextField()

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.name

# class UserResume(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     language = models.ForeignKey(Languages, on_delete=models.CASCADE)
#     award = models.ForeignKey(Awards, on_delete=models.CASCADE)
#     education = models.ForeignKey(Education, on_delete=models.CASCADE)
#     experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
#     skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
