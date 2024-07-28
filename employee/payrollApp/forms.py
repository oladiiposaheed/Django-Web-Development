from django import forms

from payrollApp.models import Employee, OnSiteEmployee
from payrollApp.models import PartTimeEmployee
from django.forms import Select, modelform_factory, modelformset_factory, TextInput

#Create Form class
class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'birthDate': forms.widgets.DateInput(attrs={'type': 'date'}),
            'hireDate': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

PartTimeEmployeeForm = modelform_factory(PartTimeEmployee, fields=['firstName', 'lastName', 'titleName'])



class DynamicPartTimeEmployeeForm(PartTimeEmployeeForm):
    def __init__(self, *args, **kwargs):
        super(DynamicPartTimeEmployeeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.pop('required', None)

class NewPartTimeEmployeeForm(forms.ModelForm):
    class Meta:
        model = PartTimeEmployee
        fields='__all__'

PartTimeEmployeeFormSet = forms.modelformset_factory(PartTimeEmployee,
                                                     form=NewPartTimeEmployeeForm,
                                                     extra=10)

class OnSiteEmployeeForm(forms.ModelForm):
    class Meta:
        model = OnSiteEmployee
        fields = ['first_name', 'last_name', 'country', 'state', 'city']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'First Name'
            }),

            'last_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Last Name'
            }),

            'country': Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Country'
            }),

            'state': Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'state'
            }),

            'city': Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'city'
            }),
        }