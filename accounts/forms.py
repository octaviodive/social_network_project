from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2', )

