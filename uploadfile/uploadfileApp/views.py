#from pyexpat.errors import messages
import os
from django.shortcuts import get_object_or_404, redirect, render
from uploadfileApp.models import EmployeeCertificate, Employee
from uploadfileApp.forms import EmployeeForm
from django.contrib import messages
# Create your views here.

def employee_create(request):
    employee_form = EmployeeForm()

    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        certificate_files = request.FILES.getlist('certificate_files')

        if employee_form.is_valid():
            employee = employee_form.save()
            if len(certificate_files) > 10:
                messages.error(request, 'You can only upload a maximum of 10 certificate files')
                return redirect('employee_create')
            
        #Create a folder for the employee using employee id
        employee_folder = os.path.join('employee_files', 'certificates', str(employee.id))
        os.makedirs(employee_folder, exist_ok=True)

        for idx, certificate_file in enumerate(certificate_files, start=1):
            original_extension = os.path.splitext(certificate_file.name)[1]

            #Rename and save the certificate file with the desired format
            new_filename = '{} {} {}{}'.format(employee.id, employee.first_name, idx, original_extension)
            new_file_path = os.path.join(employee_folder, new_filename)

            #Save the certificate file
            with open(new_file_path, 'wb+') as destination:
                for chunk in certificate_file.shunks():
                    destination.write(chunk)

            EmployeeCertificate.objects.create(employee=employee,
                                               certificate_file=new_file_path) #Save the path, not the file object


        else:
            employee_form = EmployeeForm()

    dict = {'employee_form': employee_form}
    return render(request, 'uploadfileApp/employee_create.html', dict)

    
def employee_list(request):
    employees = Employee.objects.all()

    #Calculate remaining certificates for each employee
    employee_data = []
    for employee in employees:
        existing_certificates = len(EmployeeCertificate.objects.filter(employee=employee))
        remaining_certificates = 10 - existing_certificates
        dict1 = {'employee': employee, 'remaining_certificates': remaining_certificates}
        employee_data.append(dict1)
    dict = {'employee_data': employee_data}
    return render(request, 'uploadfileApp/employee_list.html', dict)


def employee_details(request, employee_id):
    employee = Employee.get_object_or_404(Employee, pk=employee_id)
    certificates = EmployeeCertificate.objects.filter(employee=employee)
    dict = {'employee': employee, 'certificates': certificates}
    return render(request, 'uploadfileApp/employee_details.hmtl', dict)