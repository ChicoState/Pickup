from dataclasses import fields
from sys import maxsize
from urllib import request
from xml.dom import ValidationErr
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    post_loc = forms.CharField(
        label="Where are we meeting?",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter the location'})
    )
    post_title = forms.CharField(
        label="What are we playing?",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter the game title'})
    )
    post_text = forms.CharField(
        label="What's going on?",
        max_length=255,
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Enter a description'})
    )

    class Meta:
        model = models.Post
        fields = ('post_text', 'post_loc', 'post_title')
        exclude = ('author', 'rsvp_list')

    

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user