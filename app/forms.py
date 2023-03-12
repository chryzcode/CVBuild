from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.forms import ModelForm

from .models import *


class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*********'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*********'}))

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

        widgets= {    
            "email": forms.TextInput(
                attrs={"placeholder": "johndoe@gmail.com"}
            ),
            "first_name": forms.TextInput(
                attrs={"placeholder": "John"}
            ),

             "last_name": forms.TextInput(
                attrs={"placeholder": "Doe"}
            ),
        }

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
        active_user = User.objects.filter(email=email, is_active=True)
        inactive_user = User.objects.filter(email=email, is_active=True)
        if active_user.count():
            raise forms.ValidationError("Email is already taken")
        if inactive_user.count():
            inactive_user.delete()
        return email

class PasswordResetForm(PasswordResetForm):
    email = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email)
        if not user:
            raise forms.ValidationError("Account not found")
        return email
    
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'johndoe@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*********'}))


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

        widgets= {    
            "full_name": forms.TextInput(
                attrs={"placeholder": "John Doe"}
            ),
            "job_title": forms.TextInput(
                attrs={"placeholder": "Software Developer"}
            ),
             "email": forms.EmailInput(
                attrs={"placeholder": "johndoe@gmail.com"}
            ),
            "phone": forms.TextInput(
                attrs={"placeholder": "+135806600"}
            ),
            "address": forms.TextInput(
                attrs={"placeholder": "Block 44, Johnson Avenue, New York"}
            ),
             "nationality": forms.TextInput(
                attrs={"placeholder": "American"}
            ),
            "marital_status": forms.TextInput(
                attrs={"placeholder": "Single"}
            ),
            "military_service": forms.TextInput(
                attrs={"placeholder": "National Defence Academy"}
            ),
             "gender_pronoun": forms.TextInput(
                attrs={"placeholder": "He/ Him"}
            ),
            "passport_id": forms.TextInput(
                attrs={"placeholder": "9732458236"}
            ),
            "driving_license": forms.TextInput(
                attrs={"placeholder": "NY1345567"}
            ),
        }

    
    def __init__(self, *args, **kwargs):
        super(PersonalDetailsForm, self).__init__(*args, **kwargs)


class FeedbackForm(ModelForm):
    class Meta:
        models = Feedback
        exclude = ['personal_detail', 'time_created']
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        if name < 5:
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


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            # "avatar",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "John"}
            ),
             "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Doe"}
            ),
            # "avatar": forms.FileInput(attrs={"class": "form-control"}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if phone_number == None:
            raise forms.ValidationError("Field is required")
        return phone_number

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)


class LinkForm(ModelForm):
    class Meta:
        model = Personal_Details
        exclude =  ['user', 'full_name', 'job_title','email', 'phone', 'address', 'date_of_birth', 'nationality', 'passport_id', 'marital_status', 'military_service', 'driving_license', 'gender_pronoun', 'resume_name']

        widgets = {
            "website": forms.TextInput(
                attrs={"placeholder": "www.jondoe.com"}
            ),
            "twitter": forms.TextInput(
                attrs={"placeholder": "https://twitter.com/john-doe"}
            ),
            "github": forms.TextInput(
                attrs={"placeholder": "https://github.com/john-doe"}
            ),
            "linkedin": forms.TextInput(
                attrs={"placeholder": "https://linkedin.com/john-doe"}
            ),
            "medium": forms.TextInput(
                attrs={"placeholder": "johndoe.medium.com"}
            ),
             "stackoverflow": forms.TextInput(
                attrs={"placeholder": "https://stackoverflow.com/users/19129/johndoe"}
            ), "gitlab": forms.TextInput(
                attrs={"placeholder": "https://gitlab.com/john-doe"}
            ), "quora": forms.TextInput(
                attrs={"placeholder": "https://www.quora.com/profile/john-doe"}
            ), "facebook": forms.TextInput(
                attrs={"placeholder": "https://web.facebook.com/john.doe.2/"}
            ), "instagram": forms.TextInput(
                attrs={"placeholder": "https://www.instagram.com/johndoe/"}
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