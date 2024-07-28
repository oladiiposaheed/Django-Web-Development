from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.
import re
from django.core.exceptions import ValidationError

#Custom Validation
def validate_favwebsiteurl(iurl):
    pattern = re.compile(r"^http\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$")
    if not re.fullmatch(pattern, iurl):
        raise  ValidationError('Invalid URL! Example: www.google.com')

class UserRegistration(models.Model):
    #username = models.CharField(max_length=30, verbose_name='User Name')
    username = models.CharField(max_length=30, verbose_name='User Name', validators=[MinLengthValidator(4)])
    #password = models.CharField(max_length=30, verbose_name='Password')
    password = models.CharField(max_length=30, verbose_name='Password', validators=[MinLengthValidator(8)])
    #confirm_password = models.CharField(max_length=30, verbose_name='Confirm Password') 
    confirm_password = models.CharField(max_length=30, verbose_name='Confirm Password', validators=[MinLengthValidator(8)])
    gender = models.CharField(max_length=30, verbose_name='Gender')
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    country = models.CharField(max_length=30, verbose_name='Country')
    email = models.EmailField(verbose_name='Email')
    #postal_code = models.IntegerField(verbose_name='Postal Code')
    postal_code = models.IntegerField(verbose_name='Postal Code', validators=[MinValueValidator(1000),
                                                                               MaxValueValidator(9999)])
    phone_number = models.CharField(max_length=15, verbose_name='Phone Number')
    profile = models.TextField(verbose_name='User Profile', blank=True)
    website_url = models.URLField(verbose_name='Website URL')
    terms_conditions = models.BooleanField(verbose_name='Terms & Conditions')
    favwebsite_url = models.CharField(max_length=256, validators=[validate_favwebsiteurl])