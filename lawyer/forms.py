from django import forms
from django.contrib.auth.models import User
from .models import Lawyer, Blog


class LawyerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ['full_name', 'address', 'mobile', 'email', 'qualifications', 'specializations']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = [
            'years_of_experience',
            'profile_photo',
            'court_duty',
            'total_cases'
        ]
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content','image']
