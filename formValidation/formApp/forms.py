from django import forms
from formApp.models import UserRegistration
from django.forms import DateInput, EmailInput, PasswordInput, RadioSelect,Select, URLInput
#from models.formApp import 
import re

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = UserRegistration
        fields = '__all__'

        genders = [{'male', 'Male'}, {'female', 'Female'}]
        countries = [
            ('select', 'Please Choose a Country'),
            ('United Kingdom', 'United Kingdom'),
            ('Ghana', 'Ghana'),
            ('Spain', 'Spain'),
            ('Nigeria', 'Nigeria'),
            ('America', 'America'),
            ('India', 'India'),
            ('Syria', 'Syria'),
            ('Canada', 'Canada')
        ]

        widgets = {
            'password': PasswordInput(),
            'confirm_password': PasswordInput(),
            'gender': RadioSelect(choices=genders),
            'country': Select(choices=countries),
            'date_of_birth': DateInput(attrs={'type': 'date'}),
            'email': EmailInput(),
            'website_url': URLInput()
        }

    #
    def clean_phone_num(self):
        iphonenumber = self.cleaned_data.get("phone_number")
        if self.iphonenumber:
            #pattern = re.compile(r"(0|91)?[6-9][0-9]{9}")
            pattern = re.compile("[6-9][0-9]{9}")
            if re.fullmatch(pattern, iphonenumber) != None:
                raise forms.ValidationError("Invalid Phone Number! Exxample 07031224401, 08067223169")
                #print("Invalid Phone Number! Exxample 07031224401, 08067223169")
            return iphonenumber
    
    #Form level validation
    def clean(self):
        cleaned_data = super().clean()
        ipassword = cleaned_data.get('password')
        iconfirm_password = cleaned_data.get('confirm_password')
        iusername = cleaned_data.get('username')
        country = cleaned_data.get('country')
        terms_condition = cleaned_data.get('terms_conditions')

        if ipassword is not None and iusername != None:
            if ipassword == iusername:
                raise forms.ValidationError('Password and Username must not match')

        if ipassword and iconfirm_password:
            if ipassword != iconfirm_password:
                raise forms.ValidationError('Passwords must match.')
        
        if country == 'select':
            raise forms.ValidationError('Please choose a country')

        if not terms_condition:
            raise forms.ValidationError('Please agree to the terms and conditions')

        return cleaned_data