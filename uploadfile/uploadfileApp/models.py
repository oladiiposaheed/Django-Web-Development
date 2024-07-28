from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    cv_file = models.FileField(upload_to='employee_files/cv', null=True, blank=True)
    photo_file = models.FileField(upload_to='employee_files/photo', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.id, self.first_name)
    
def certificate_upload_path(instance, filename):
    return 'employee_files/certificates/{}/{}'.format(instance.employee.id, filename)

class EmployeeCertificate(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to=certificate_upload_path, null=True, blank=True)

    def __Str__(self):
        return '{}'.format(self.employee)