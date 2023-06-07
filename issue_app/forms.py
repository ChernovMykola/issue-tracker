from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import (
    Issue,
    UserProfileInfo
)


class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = UserProfileInfo
        fields = ('username', 'email', 'confirm_password')

class IssueForm(forms.ModelForm):
    name = forms.CharField()
    text = forms.Textarea()
    class Meta():
        model = Issue
        fields = ('name', 'text')

