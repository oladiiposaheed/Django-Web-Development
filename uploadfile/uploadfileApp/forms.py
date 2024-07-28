from django import forms
from uploadfileApp.models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'cv_file', 'photo_file']
