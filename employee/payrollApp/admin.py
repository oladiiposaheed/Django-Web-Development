from django.contrib import admin
from payrollApp.models import City, Employee, OnSiteEmployee, State

# Register your models here.

admin.site.register(Employee)
admin.site.register(OnSiteEmployee)
admin.site.register(State)
admin.site.register(City)