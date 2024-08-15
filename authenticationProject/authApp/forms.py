from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authApp.models import CustomUser


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=60, required=True)
    country = forms.ChoiceField(choices=CustomUser.COUNTRY_CHOICES, required=True)
    address = forms.CharField(max_length=60, required=True)

    class Meta:
        #model = User
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'country', 'address']

class ChangeProfileForm(UserChangeForm):
    password = None #Exclude password field
    username = forms.CharField(disabled=True)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=60, required=True)
    last_name = forms.CharField(max_length=60, required=True)
    country = forms.ChoiceField(choices=CustomUser.COUNTRY_CHOICES, required=True)
    address = forms.CharField(max_length=60, required=True)

    class Meta:
        #model = User
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'country', 'address']