from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django import forms
from django.forms import ModelForm, widgets
from .models import User, Event, Comment, Message, Venue, Artist

class brrRegForm(forms.ModelForm):
    BOOKER = 'BKR'
    ARTIST = 'ART'
    ACCESS_CHOICES = (
        (BOOKER, 'Booker'),
        (ARTIST, 'Artist')
        )
    username = forms.CharField(widget=forms.widgets.TextInput, label="Username")
    first_name = forms.CharField(widget=forms.widgets.TextInput, label="First Name")
    last_name = forms.CharField(widget=forms.widgets.TextInput, label="Last Name")
    email = forms.EmailField(widget=forms.widgets.TextInput,label="Email")
    user_phone = forms.CharField(widget=forms.widgets.TextInput,label="Contact Phone")
    groups = forms.ChoiceField(widget=forms.widgets.Select, choices=ACCESS_CHOICES, label="Access")
    password1 = forms.CharField(widget=forms.widgets.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.widgets.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'user_phone', 'groups', 'password1', 'password2']

    def clean(self):
        cleaned_data = super(brrRegForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            print "inside Clean for passwords"
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(brrRegForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        print commit, "this is the commit in save"
        if commit:
            user.save()
        print user
        return user

class brrLogForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.widgets.TextInput)
    password = forms.CharField(label='Password', widget=forms.widgets.PasswordInput)
    class Meta:
        fields = ['username', 'password']

class NewEventForm(forms.ModelForm):
    artist_id = forms.CharField(widget=forms.widgets.HiddenInput)
    status = forms.CharField(widget=forms.widgets.HiddenInput)
    venue_id = forms.CharField(label='Venue', widget=forms.widgets.Select)
    event_date = forms.CharField(label='Event Date',widget=forms.widgets.DateInput)


class ArtistForm(forms.ModelForm):
    artist_name = forms.CharField(label='Artist Name', widget=forms.widgets.TextInput)
    site = forms.URLField(label='Website', widget=forms.widgets.TextInput, required=False)
    sound = forms.URLField(label='Sample Sound', widget=forms.widgets.TextInput, required=False)
    artist_photo = forms.ImageField(label='Artist Photo', required=False)
    class Meta:
        model = Artist
        fields = ['artist_name', 'site', 'sound', 'artist_photo']
