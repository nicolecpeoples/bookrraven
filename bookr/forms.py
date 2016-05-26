from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms import ModelForm
from .models import People
from django import forms

class bbrRegForm(UserCreationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='email address')
    access = forms.ChoiceField(choices=People.ACCESS_CHOICES)
    user_phone = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name', 'email', 'user_phone' 'access', 'password1', 'password2')
       
    def save(self, commit=True):
        user = super(bbrRegForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']       
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.access = self.cleaned_data['access']
        if commit:
            user.save()
            return user