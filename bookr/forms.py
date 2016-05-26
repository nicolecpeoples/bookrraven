from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    BOOKER = 'BKR'
	ARTIST = 'ART'
	ACCESS_CHOICES = (
		(BOOKER, 'Booker'),
		(ARTIST, 'Artist')
		)
    # first_name = forms.CharField(label='First Name', max_length=45)
    # last_name = forms.CharField(label='Last Name', max_length=45)
    # email = forms.EmailField(label='Email Address')
    phone = forms.ChoiceField(max_length=10)
    access = models.ChoiceField(choices=ACCESS_CHOICES)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'access', 'password1', 'password2')
    def save(self, commit=True)
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.access = self.cleaned_data['access']       
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            return user