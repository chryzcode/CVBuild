from django import forms
from .models import Person, Awards, Education, Experience, Skills, Project, Volunteer
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class EditAccountForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class PasswordChangingForm(PasswordChangeForm):
        old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
        new_password1 = forms.CharField(max_length = 100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
        new_password2 = forms.CharField(max_length = 100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

        class Meta:
                model = User
                fields = ('old_password', 'new_password1', 'new_password2')

class PersonForm(forms.ModelForm):
    class Meta:
        model= Person
        exclude = ["user"]
        fields=['name', 'location', 'email', 'mobile_number', 'occupation', 'site', 'twitter_url', 'github_url', 'linkedin_url', 'dribble_url', 'figma_url', 'codepen_url', 'behance_url', 'summary']

        widgets={
                'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'My name'}),
                'location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location  e.g  Lagos, Nigeria'}),
                'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email address'}),
                'mobile_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mobile Number'}),
                'occupation':forms.TextInput(attrs={'class':'form-control', 'placeholder':'My occupation'}),
                'site':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Porfolio Link, Website'}),
                'twitter_url':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Twitter Account URL. If none leave blank'}),
                'github_url':forms.TextInput(attrs={'class':'form-control', 'placeholder':'GitHub Account URL. If none leave blank'}),
                'linkedin_url':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Linkedin Account URL. If none leave blank'}),
                'dribble_url':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dribble Account URL. If none leave blank'}),
                'figma_url':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Figma Account URL. If none leave blank'}),
                'codepen_url':forms.TextInput(attrs={'class':'form-control', 'placeholder':'CodePen Account URL. If none leave blank'}),
                'behance_url':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Behance Account URL. If none leave blank'}),
                'summary':forms.Textarea(attrs={'class':'form-control', 'placeholder':'About Me'}),
        }


class SkillsForm(forms.ModelForm):
    class Meta:
        model= Skills
        exclude = ["user"]
        fields=['name']

        widgets={
                'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'My Skills  Python, Django, Laravel'}),
        }

class AwardForm(forms.ModelForm):
    class Meta:
        model= Awards
        exclude = ["user"]
        fields=['award']

        widgets={
                'award':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Awards received'}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model= Experience
        exclude = ["user"]
        fields=['company_name', 'company_location', 'post_held', 'year_from', 'year_to', 'info']

        widgets={
                'company_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company name'}),
                'company_location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company location'}),
                'post_held':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Position held'}),
                'year_from':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Month and year started '}),
                'year_to':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Month and year ended. If ONGOING, leave it blank'}),
                'info':forms.Textarea(attrs={'class':'form-control', 'placeholder':'More information'}),
        }

class VolunteerForm(forms.ModelForm):
    class Meta:
        model= Volunteer
        exclude = ["user"]
        fields=['post_held', 'organization', 'year_from', 'year_to', 'info']

        widgets={
                'post_held':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Position held'}),
                'organization':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Organization name'}),                
                'year_from':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Month and year started'}),
                'year_to':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Month and year ended. If ONGOING, leave it blank'}),
                'info':forms.Textarea(attrs={'class':'form-control', 'placeholder':'More information'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model= Project
        exclude = ["user"]
        fields=['name', 'source_code', 'live', 'info']

        widgets={
                'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Project name'}),
                'source_code':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Github, Gitlab, BitBucket source code'}),
                'live':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Github Pages, Netlify, Heroku hosted link'}),
                'info':forms.Textarea(attrs={'class':'form-control', 'placeholder':'More information'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model= Education
        exclude = ["user"]
        fields=['school_name', 'school_location', 'degree', 'year_from', 'year_to', 'info']

        widgets={
                'school_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'School name'}),
                'school_location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'School Location'}),
                'degree':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Degree SSCE Neco Bsc'}),
                'year_from':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Month and year started'}),
                'year_to':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Month and year ended. If ONGOING, leave it blank'}),
                'info':forms.Textarea(attrs={'class':'form-control', 'placeholder':'More information'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__ (self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'