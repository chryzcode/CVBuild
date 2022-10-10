from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.forms import ModelForm

from .models import *


class RegistrationForm(ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if first_name is None:
            raise forms.ValidationError("This field is required.")
        return first_name
        
    
    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if last_name is None:
            raise forms.ValidationError("This field is required.")
        return last_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords do not match.")
        return cd["password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        r = User.objects.filter(email=email)
        if r.count():
            raise forms.ValidationError("Email is already taken")
        return email

class PasswordResetForm(PasswordResetForm):
    email = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email)
        if not user:
            raise forms.ValidationError("Account not found")
        return email


class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["new_password1"] != cd["new_password2"]:
            raise forms.ValidationError("Passwords do not match.")
        return cd["new_password2"]

class PersonalDetailsForm(ModelForm):
    class Meta:
        model = Personal_Details
        exclude =  ['user']
    
    def __init__(self, *args, **kwargs):
        super(PersonalDetailsForm, self).__init__(*args, **kwargs)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude =  ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

class LinkForm(ModelForm):
    class Meta:
        model = Personal_Details
        exclude =  ['user', 'full_name', 'job_title','email', 'phone', 'address', 'date_of_birth', 'nationality', 'passport_id', 'marital_status', 'military_service', 'driving_license', 'gender_pronoun']
    
    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.label_suffix = "" 

class SkillForm(ModelForm):
    class Meta:
        model = Skills
        exclude =  ['personal_detail']

    def clean_skill(self):
        skill = self.cleaned_data["skill"]
        if skill == None:
            raise forms.ValidationError("Field is required")
        return skill
    
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

