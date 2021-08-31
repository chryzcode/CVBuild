from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
        class Meta:
                model= Profile
                fields=['name', 'email', 'phone', 'summary', 'education', 'skills', 'experience']

                widgets={
                        'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}),
                        'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email'}),
                        'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mobile Number'}),
                        'summary':forms.Textarea(attrs={'class':'form-control', 'placeholder':'About me'}),
                        'education':forms.Textarea(attrs={'class':'form-control', 'placeholder':'My Education'}),
                        'skills':forms.Textarea(attrs={'class':'form-control', 'placeholder':'My Skills'}),
                        'experience':forms.Textarea(attrs={'class':'form-control', 'placeholder':'My Experience'}),
                }