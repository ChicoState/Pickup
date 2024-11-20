from dataclasses import fields
from sys import maxsize
from urllib import request
from xml.dom import ValidationErr
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CAT_CHOICES = (
    ('Choose a Category', 'Choose a Category'),
    ('Sports', 'Sports'),
    ('Gaming', 'Video Games'),
)

SPORT_CHOICES = (
    ('Basketball', 'Basketball'),
    ('Football', 'Football'),
    ('Soccer', 'Soccer'),
)

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
    event_time = forms.DateTimeField(
        label="When is it happening?",
        required=True,  # required, or not since it'll default to the current time if left blank?
        widget=forms.DateTimeInput(attrs={'id': 'datetime-picker', 'placeholder': 'Select date and time'})  # Bind the date-time picker:
    )
    post_tags = forms.CharField(
        label="Any tags?",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Any Tags?'})
        )
    catergory= forms.CharField(label='Choose a Category', widget=forms.Select(choices=CAT_CHOICES))
    sportcatergory= forms.CharField(label='Choose a Sport', widget=forms.Select(choices=SPORT_CHOICES))
    class Meta:
        model = models.Post
        fields = ('post_text', 'catergory','post_loc', 'post_title', 'post_tags', 'event_time')
        exclude = ('author', 'rsvp_list')

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