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


class FeedbackForm(ModelForm):
    class Meta:
        models = Feedback
        exclude = ['personal_detail', 'time_created']
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        if name == None:
            raise forms.ValidationError("Field is required")
        return name

    def clean_comment(self):
        comment = self.cleaned_data["comment"]
        if comment == None:
            raise forms.ValidationError("Field is required")
        return comment

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude =  ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)




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


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)


class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)


class ReferenceForm(ModelForm):
    class Meta:
        model = Reference
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(ReferenceForm, self).__init__(*args, **kwargs)


class AwardForm(ModelForm):
    class Meta:
        model = Award
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(AwardForm, self).__init__(*args, **kwargs)


class OrganisationForm(ModelForm):
    class Meta:
        model = Organisation
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(OrganisationForm, self).__init__(*args, **kwargs)

class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(CertificateForm, self).__init__(*args, **kwargs)


class InterestForm(ModelForm):
    class Meta:
        model = Interest
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(InterestForm, self).__init__(*args, **kwargs)


class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(PublicationForm, self).__init__(*args, **kwargs)


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ['personal_detail']
    
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)


class LinkForm(ModelForm):
    class Meta:
        model = Personal_Details
        exclude =  ['user', 'full_name', 'job_title','email', 'phone', 'address', 'date_of_birth', 'nationality', 'passport_id', 'marital_status', 'military_service', 'driving_license', 'gender_pronoun', 'resume_name']

        widgets = {
            "website": forms.TextInput(
                attrs={"placeholder": " Website"}
            ),
            "twitter": forms.TextInput(
                attrs={"placeholder": "Twitter"}
            ),
            "github": forms.TextInput(
                attrs={"placeholder": "Github"}
            ),
            "linkedin": forms.TextInput(
                attrs={"placeholder": "Linkedin"}
            ),
            "medium": forms.TextInput(
                attrs={"placeholder": "Medium"}
            ),
             "stackoverflow": forms.TextInput(
                attrs={"placeholder": "Stackoverflow"}
            ), "gitlab": forms.TextInput(
                attrs={"placeholder": "Gitlab"}
            ), "quora": forms.TextInput(
                attrs={"placeholder": "Quora"}
            ), "facebook": forms.TextInput(
                attrs={"placeholder": "Facebook"}
            ), "instagram": forms.TextInput(
                attrs={"placeholder": "Instagram"}
            ), "hackerrank": forms.TextInput(
                attrs={"placeholder": "Hackerrank"}
            ), "wechat": forms.TextInput(
                attrs={"placeholder": "Wechat"}
            ), "kaggle": forms.TextInput(
                attrs={"placeholder": "Kaggle"}
            ), "youtube": forms.TextInput(
                attrs={"placeholder": "Youtube"}
            ), "tiktok": forms.TextInput(
                attrs={"placeholder": "Tiktok"}
            ), "signal": forms.TextInput(
                attrs={"placeholder": "Signal"}
            ), "telegram": forms.TextInput(
                attrs={"placeholder": "Telegram"}
            ), "whatsapp": forms.TextInput(
                attrs={"placeholder": "Whatsapp"}
            ), "paypal": forms.TextInput(
                attrs={"placeholder": "Paypal"}
            ), "dev_to": forms.TextInput(
                attrs={"placeholder": "Dev.to"}
            ), "angellist": forms.TextInput(
                attrs={"placeholder": "Angellist"}
            ), "producthunt": forms.TextInput(
                attrs={"placeholder": "Producthunt"}
            ), "artstation": forms.TextInput(
                attrs={"placeholder": "Artstation"}
            ), "codepen": forms.TextInput(
                attrs={"placeholder": "Codepen"}
            ),
            "fiverr": forms.TextInput(
                attrs={"placeholder": "Fiverr"}
            ),"hashnode": forms.TextInput(
                attrs={"placeholder": "Hashnode"}
            ),"pluralsight": forms.TextInput(
                attrs={"placeholder": "Pluralsight"}
            ),"researchgate": forms.TextInput(
                attrs={"placeholder": "Researchgate"}
            ),"imdb": forms.TextInput(
                attrs={"placeholder": "Imdb"}
            ),"qwiklabs": forms.TextInput(
                attrs={"placeholder": "Qwiklabs"}
            ),"googleplay": forms.TextInput(
                attrs={"placeholder": "Googleplay"}
            ),"tumbir": forms.TextInput(
                attrs={"placeholder": "Tumbir"}
            ),"tripadvisor": forms.TextInput(
                attrs={"placeholder": "Tripadvisor"}
            ),"yelp": forms.TextInput(
                attrs={"placeholder": "Yelp"}
            ),"qq": forms.TextInput(
                attrs={"placeholder": "QQ"}
            ),"slack": forms.TextInput(
                attrs={"placeholder": "Slack"}
            ),"flickr": forms.TextInput(
                attrs={"placeholder": "Flickr"}
            ),"reverbnation": forms.TextInput(
                attrs={"placeholder": "Reverbnation"}
            ),"deviantart": forms.TextInput(
                attrs={"placeholder": "Deviantart"}
            ),"vimeo": forms.TextInput(
                attrs={"placeholder": "Vimeo"}
            ),"reddit": forms.TextInput(
                attrs={"placeholder": "Reddit"}
            ),"pininterest": forms.TextInput(
                attrs={"placeholder": "Pininterest"}
            ),"blogger": forms.TextInput(
                attrs={"placeholder": "Blogger"}
            ),"spotify": forms.TextInput(
                attrs={"placeholder": "Spotify"}
            ),"bitcoin": forms.TextInput(
                attrs={"placeholder": "Bitcoin"}
            ),"appstore": forms.TextInput(
                attrs={"placeholder": "Appstore"}
            ),"wordpress": forms.TextInput(
                attrs={"placeholder": "Wordpress"}
            ),"leetcode": forms.TextInput(
                attrs={"placeholder": "Leetcode"}
            ),"codechef": forms.TextInput(
                attrs={"placeholder": "Codechef"}
            ),"codeforces": forms.TextInput(
                attrs={"placeholder": "Codeforces"}
            ),"vsco": forms.TextInput(
                attrs={"placeholder": "Vsco"}
            ),"snapchat": forms.TextInput(
                attrs={"placeholder": "Snapchat"}
            ),"upwork": forms.TextInput(
                attrs={"placeholder": "Upwork"}
            ),"geeksforgeeks": forms.TextInput(
                attrs={"placeholder": "Geeksforgeeks"}
            ),"googlescholar": forms.TextInput(
                attrs={"placeholder": "Googlescholar"}
            ),"line": forms.TextInput(
                attrs={"placeholder": "Line"}
            ),"tryhackme": forms.TextInput(
                attrs={"placeholder": "Tryhackme"}
            ),"coursera": forms.TextInput(
                attrs={"placeholder": "Coursera"}
            ),"protonmail": forms.TextInput(
                attrs={"placeholder": "Protonmail"}
            ),"hackerearth": forms.TextInput(
                attrs={"placeholder": "Hackerearth"}
            ),"codewars": forms.TextInput(
                attrs={"placeholder": "Codewars"}
            ),"hackthebox": forms.TextInput(
                attrs={"placeholder": "Hackthebox"}
            ),"bitbucket": forms.TextInput(
                attrs={"placeholder": "Bitbucket"}
            ),"gitea": forms.TextInput(
                attrs={"placeholder": "Gitea"}
            ),"xing": forms.TextInput(
                attrs={"placeholder": "Xing"}
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.label_suffix = "" 
        self.fields["dev_to"].label = "Dev.to"
        self.fields["qq"].label = "QQ"