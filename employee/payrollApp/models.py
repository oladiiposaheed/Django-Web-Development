from django.db import models

# Create your models here.

class Department(models.Model):
    dept = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.dept
    
class Country(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country

class Employee(models.Model):

    COUNTRIES = [('NIG', 'Nigeria'), ('UK', 'United Kingdom'), ('SA', 'Saudi Arabia'),
                 ('USA', 'United State of America'), ('AUS', 'Australia'), ('RS', 'Russia'),
                 ('AU', 'Austria'), ('GN', 'Ghana'), ('MO', 'Morocco'), ('SD', 'Sudan'), ('SP', 'Spain')
            ]
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    titleName = models.CharField(max_length=60)
    hasPassport = models.BooleanField()
    salary = models.FloatField()
    birthDate = models.DateField()
    hireDate = models.DateField()
    notes = models.CharField(max_length=300)
    #country = models.CharField(max_length=60, choices=COUNTRIES, default=None)
    email = models.EmailField(max_length=100, default='')
    phoneNumber = models.CharField(max_length=20, default='')
    empDept = models.ForeignKey('Department', default=0, on_delete=models.PROTECT, related_name='Departments')
    empCountry = models.ForeignKey('Country', default=0, on_delete=models.PROTECT, related_name='Countrys')
    
class PartTimeEmployee(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    titleName = models.CharField(max_length=60)


class State(models.Model):
    name = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=100, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, default=None)

    def __Str__(self):
        return self.name
    
class OnSiteEmployee(models.Model):
    first_name = models.CharField(max_length=60, null=True)
    last_name = models.CharField(max_length=60, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default=None)
    state = models.ForeignKey(State, on_delete=models.PROTECT, default=None)
    city = models.ForeignKey(City, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.first_name