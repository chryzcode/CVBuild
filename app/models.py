from django.db import models

# Create your models here.
from email.policy import default
from os import link
from django.db import models
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
# Create your models here.


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_("The email field is required"))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to="user-profile-images/", null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email


class Personal_Details(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length=300)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=200, null=True, blank=True)
    passport_id = models.CharField(max_length=200, null=True, blank=True)
    marital_status = models.CharField(max_length=200, null=True, blank=True)
    military_service = models.CharField(max_length=200, null=True, blank=True)
    driving_license = models.CharField(max_length=200, null=True, blank=True)
    gender_pronoun = models.CharField(max_length=200, null=True, blank=True)

    def __str__ (self):
        return self.full_name + ' personal details' 

class Links(models.Model):
    personal_detail = models.ForeignKey(Personal_Details, on_delete=models.CASCADE)
    website = models.CharField(max_length=700, null=True, blank=True)
    twitter = models.CharField(max_length=250, null = True, blank = True)
    github = models.CharField(max_length=250, null = True, blank = True)
    linkedin = models.CharField(max_length=250, null = True, blank = True)
    medium = models.CharField(max_length=250, null = True, blank = True)
    orcid = models.CharField(max_length=250, null = True, blank = True)
    skype = models.CharField(max_length=250, null = True, blank = True)
    discord = models.CharField(max_length=250, null = True, blank = True)
    dribble = models.CharField(max_length=250, null = True, blank = True)
    behance = models.CharField(max_length=250, null = True, blank = True)
    medium = models.CharField(max_length=250, null = True, blank = True)
    stackoverflow = models.CharField(max_length=250, null = True, blank = True)
    gitlab = models.CharField(max_length=250, null = True, blank = True)
    quora = models.CharField(max_length=250, null = True, blank = True)
    facebook = models.CharField(max_length=250, null = True, blank = True)
    instagram = models.CharField(max_length=250, null = True, blank = True)
    hackerrank = models.CharField(max_length=250, null = True, blank = True)
    wechat = models.CharField(max_length=250, null = True, blank = True)
    kaggle = models.CharField(max_length=250, null = True, blank = True)
    youtube = models.CharField(max_length=250, null = True, blank = True)
    tiktok = models.CharField(max_length=250, null = True, blank = True)
    signal = models.CharField(max_length=250, null = True, blank = True)
    telegram = models.CharField(max_length=250, null = True, blank = True)
    whatsapp = models.CharField(max_length=250, null = True, blank = True)
    paypal = models.CharField(max_length=250, null = True, blank = True)
    dev_to = models.CharField(max_length=250, null = True, blank = True)
    angellist = models.CharField(max_length=250, null = True, blank = True)
    producthunt = models.CharField(max_length=250, null = True, blank = True)
    artstation = models.CharField(max_length=250, null = True, blank = True)
    codepen = models.CharField(max_length=250, null = True, blank = True)
    fiverr = models.CharField(max_length=250, null = True, blank = True)
    hashnode = models.CharField(max_length=250, null = True, blank = True)
    pluralsight = models.CharField(max_length=250, null = True, blank = True)
    researchgate = models.CharField(max_length=250, null = True, blank = True)
    imdb = models.CharField(max_length=250, null = True, blank = True)
    qwiklabs = models.CharField(max_length=250, null = True, blank = True)
    googleplay = models.CharField(max_length=250, null = True, blank = True)
    tumbir = models.CharField(max_length=250, null = True, blank = True)
    tripadvisor = models.CharField(max_length=250, null = True, blank = True)
    yelp = models.CharField(max_length=250, null = True, blank = True)
    qq = models.CharField(max_length=250, null = True, blank = True)
    slack = models.CharField(max_length=250, null = True, blank = True)
    flickr = models.CharField(max_length=250, null = True, blank = True)
    reverbnation = models.CharField(max_length=250, null = True, blank = True)
    deviantart = models.CharField(max_length=250, null = True, blank = True)
    vimeo = models.CharField(max_length=250, null = True, blank = True)
    reddit = models.CharField(max_length=250, null = True, blank = True)
    pininterest = models.CharField(max_length=250, null = True, blank = True)
    blogger = models.CharField(max_length=250, null = True, blank = True)
    spotify = models.CharField(max_length=250, null = True, blank = True)
    bitcoin = models.CharField(max_length=250, null = True, blank = True)
    appstore = models.CharField(max_length=250, null = True, blank = True)
    wordpress = models.CharField(max_length=250, null = True, blank = True)
    leetcode = models.CharField(max_length=250, null = True, blank = True)
    codechef = models.CharField(max_length=250, null = True, blank = True)
    codeforces = models.CharField(max_length=250, null = True, blank = True)
    vsco = models.CharField(max_length=250, null = True, blank = True)
    sanpchat = models.CharField(max_length=250, null = True, blank = True)
    upwork = models.CharField(max_length=250, null = True, blank = True)
    geeksforgeeks = models.CharField(max_length=250, null = True, blank = True)
    googlescholar = models.CharField(max_length=250, null = True, blank = True)
    line = models.CharField(max_length=250, null = True, blank = True)
    tryhackme = models.CharField(max_length=250, null = True, blank = True)
    coursera = models.CharField(max_length=250, null = True, blank = True)
    protonmail = models.CharField(max_length=250, null = True, blank = True)
    hackerearth = models.CharField(max_length=250, null = True, blank = True)
    codewars = models.CharField(max_length=250, null = True, blank = True)
    hackthebox = models.CharField(max_length=250, null = True, blank = True)
    bitbucket = models.CharField(max_length=250, null = True, blank = True)
    gitea = models.CharField(max_length=250, null = True, blank = True)
    xing = models.CharField(max_length=250, null = True, blank = True)
    
    def __str__(self):
        return self.full_name + ' ' + self.links

class Profile(models.Model):
    personal_detail = models.ForeignKey(Personal_Details, on_delete=models.CASCADE)
    summary = RichTextField()  

    def __str__(self):
        return self.personal_detail.full_name + ' profile'

class Skill_Level(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name + ' skill level'

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    skill = models.CharField(max_length=80)
    information = models.CharField(max_length=200)
    level = models.ForeignKey(Skill_Level, on_delete=models.CASCADE)

    def __str__ (self):
        return self.name

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    job_title = models.CharField(max_length=200)
    employer = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank= True, null= True)
    country = models.CharField(max_length=100, blank= True, null= True)
    company_location = models.CharField(max_length=200, blank= True, null= True)
    start_date = models.DateField(blank= True, null= True)
    end_date = models.DateField(blank= True, null= True)
    description = RichTextField(blank= True, null= True)
    current = models.BooleanField(default=False)
    link = models.CharField(max_length = 300, blank= True, null= True)

    def __str__ (self):
        return self.employer + ' experience'


class Project(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    project_title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100, blank= True, null= True)
    start_date = models.DateField(blank= True, null= True)
    end_date = models.DateField(blank= True, null= True)
    description = RichTextField(blank= True, null= True)
    link = models.CharField(max_length = 300, blank= True, null= True)

    def __str__ (self):
        return self.name

class Education(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    school = models.CharField(max_length=30)
    degree = models.CharField(max_length=100, blank= True, null= True)
    city = models.CharField(max_length=100, blank= True, null= True)
    country = models.CharField(max_length=100, blank= True, null= True)
    start_date = models.DateField(blank= True, null= True)
    end_date = models.DateField(blank= True, null= True)
    description = RichTextField(blank= True, null= True)
    current = models.BooleanField(default=False)
    link = models.CharField(max_length = 300, blank= True, null= True)

    def get_absolute_url(self):
        return reverse('resume')

    def __str__ (self):
        return self.school_name

class Language_Level(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name + ' language level'

class Language(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    language = models.CharField(max_length= 200)
    additional_information = models.CharField(max_length=400)
    level = models.ForeignKey(Language_Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.language + ' language'

class Reference(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    job_title = models.CharField(max_length=150, blank= True, null= True)
    organisation = models.CharField(max_length=150, blank= True, null= True)
    phone = models.CharField(max_length=15, blank= True, null= True)
    email = models.EmailField(blank= True, null= True)
    link = models.CharField(max_length=300, blank= True, null= True)

    def __str__(self):
        return self.name + ' reference'


class Award(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    award = models.CharField(max_length=150)
    issuer = models.CharField(max_length=150, blank= True, null= True)
    description = RichTextField(blank= True, null= True)
    date = models.DateField(blank= True, null= True)
    link = models.CharField(max_length=300, blank= True, null= True)

    def __str__ (self):
        return self.award + ' award'

class Organisation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    position = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank= True, null= True)
    country = models.CharField(max_length=100, blank= True, null= True)
    start_date = models.DateField(blank= True, null= True)
    end_date = models.DateField(blank= True, null= True)
    description = RichTextField(blank= True, null= True)
    current = models.BooleanField(default=False)
    link = models.CharField(max_length=300, blank= True, null= True)

    def __str__ (self):
        return self.positon + ' in f{self.organization}'

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    certificate = models.CharField(max_length = 150)
    additional_information = RichTextField(blank= True, null= True)
    link = models.CharField(max_length = 300, blank= True, null= True)

    def __str__ (self):
        return self.certificate + ' certificate'


class Interest(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    interest = models.CharField(max_length = 150)
    additional_information = RichTextField(blank= True, null= True)
    link = models.CharField(max_length = 300, blank= True, null= True)

    def __str__ (self):
        return self.interest + ' interest'


class Publication(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    publisher = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.DateField(blank= True, null= True)
    description = RichTextField(blank= True, null= True)
    link = models.CharField(max_length = 300, blank= True, null= True)

    def __str__ (self):
        return self.publisher + ' ' + self.title
