from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
#from employee.payrollApp.forms import EmployeeForm # type: ignore
#from forms import EmployeeForm
from payrollApp.forms import EmployeeForm, PartTimeEmployeeFormSet
from payrollApp.models import City, Employee, PartTimeEmployee, State

from payrollApp.forms import PartTimeEmployeeForm, OnSiteEmployeeForm

from django.core.paginator import Paginator, PageNotAnInteger
from django.conf import settings
from django.db.models import Q
from django.db import transaction

# Create your views here.

def employeeList(request):
    #employees = Employee.objects.all()
    employees = Employee.objects.select_related('empDept', 'empCountry').all()
    print(employees.query)
    templatefile = 'payrollApp/emplist.html'
    dict = {'emps': employees}
    return render(request, templatefile, context=dict)

def employeeDetails(request, id):
    #employee = Employee.objects.get(id=id)
    employee = Employee.objects.select_related('empDept', 'empCountry').all().filter(id=id)
    templatename = 'payrollApp/empdetails.html'
    dict = {'employee': employee[0]}
    return render(request, templatename, context=dict)

def employeeDelete(request, id):
    #employee = Employee.objects.get(id=id)
    templatename = 'payrollApp/empdelete.html'
    employee = Employee.objects.select_related('empDept', 'empCountry').all().filter(id=id)
    dict = {'employee': employee[0]}

    if request.method == 'POST':
        employee.delete()
        return redirect('employeelist')

    return render(request, templatename, context=dict)

def employeeUpdate(request, id):
    #employee = Employee.objects.get(id=id)
    employee = Employee.objects.select_related('empDept', 'empCountry').all().filter(id=id)
    #form = EmployeeForm(instance=employee)
    for emp in employee:
        form = EmployeeForm(instance=emp)
    templatefile = 'payrollApp/empupdate.html'
    dict = {'form': form}

    #form = EmployeeForm(request.POST, instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
        return redirect('employeelist')

    return render(request, templatefile, context=dict)

def employeeInsert(request):
    form = EmployeeForm()
    dict = {'form': form}
    templatefile = 'payrollApp/empinsert.html'

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employeelist')

    return render(request, templatefile, dict)

def BulkInsert(request):
    extra_forms = 5
    forms = [PartTimeEmployeeForm(request.POST or None, prefix=f'employee-{i}') for i in range(extra_forms)]
    Status = ""

    if request.method == 'POST':
        for form in forms:
            if form.is_valid() and form.cleaned_data.get('firstName', ''):
                form.save()
                Status = 'Records were inserted successfully'

    dict = {'forms': forms, 'extra_forms': range(extra_forms), 'Status': Status}
    return render(request, 'payrollApp/parttimeemp.html', dict)

def NewBulkInsert(request):

    if request.method == 'POST':
        formset = PartTimeEmployeeFormSet(request.POST, prefix='employee')
        if formset.is_valid():
            employees = formset.save(commit=False)
            PartTimeEmployee.objects.bulk_create(employees)
            return redirect('newbulkinsert')
        
    else:
        formset = PartTimeEmployeeFormSet(queryset=PartTimeEmployee.objects.none(), prefix='employee')
    dict = {'formset':formset}
    return render(request, 'payrollApp/newinsert.html', dict)

def BulkUpdate(request):
    employees = PartTimeEmployee.objects.all()

    forms = [PartTimeEmployeeForm(request.POST or None, 
                                  instance=employee,
                                  prefix=f'employee-{employee.id}') for employee in employees]
    if request.method == 'POST':
        updated_data = []
        
        for form in forms:
            if form.is_valid():
                employee = form.instance
                employee.firstName = form.cleaned_data['firstName']
                employee.lasstName = form.cleaned_data['lastName']
                employee.titleName = form.cleaned_data['titleName']
                updated_data.append(employee)

        PartTimeEmployee.objects.bulk_update(updated_data, ['firstName', 'lastName', 'titleName'])

    dict = {'employees': employees, 'forms': forms}
    return render(request, 'payrollApp/bulkupdate.html', dict)

def BulkDelete(request):
    employees = PartTimeEmployee.objects.all()

    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')

        if selected_ids:
            PartTimeEmployee.objects.filter(pk__in=selected_ids).delete()
            return redirect('bulkdelete')

    dict = {'employees': employees}
    return render(request, 'payrollApp/bulkdelete.html', dict)

    
def PageEmployeeList(request):
    page_size = int(request.GET.get('page_size', getattr(settings, 'PAGE_SIZE', 5)))
    page = request.GET.get('page', 1)

    search_query = request.GET.get('search', '')

    #Get the sorting parameters from the request's query paramaters
    sort_by = request.GET.get('search', '')
    sort_order = request.GET.get('sort_order', 'asc')

    valid_sort_fields = ['id', 'firstName', 'lastName', 'titleName']
    if sort_by not in valid_sort_fields:
        sort_by = 'id'

   # employees = PartTimeEmployee.objects.all()

   #Query employees based on the search query
    employees = PartTimeEmployee.objects.filter(
        Q(id__icontains=search_query) |
        Q(firstName__icontains=search_query) |
        Q(lastName__icontains=search_query) |
        Q(titleName=search_query)
    )

    #Apply sorting
    if sort_order == 'desc':
        employees = employees.order_by(f'-{sort_by}')
    else:
        employees = employees.order_by(sort_by)

    paginator = Paginator(employees, page_size)

    try:
        employees_page = paginator.page(page)
    except PageNotAnInteger:
        employees_page = paginator.page(1)
    dict = {'employees_page': employees_page, 
            'page_size': page_size, 
            'search_query': search_query,
            'sort_by': sort_by,
            'sort_order': sort_order}
    return render(request, 'payrollApp/emp_page.html', dict)


def cascadingSelect(request):
    employee_form = OnSiteEmployeeForm()

    if request.method == 'POST':
        employee_form = OnSiteEmployeeForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            return JsonResponse({'success': True})

    #dict = {'employee_form': employee_form}

    return render(request, 'payrollApp/cascading.html', {'employee_form': employee_form})

def load_state(request):
    country_id = request.GET.get('country_id')
    print(country_id)
    states = State.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse(list(states), safe=False)

def load_city(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)

def Transaction(request):

    try:
        with transaction.atomic():
            employee = PartTimeEmployee.objects.create(firstName='Mary', lastName='James', titleName='Referee')
            employee = PartTimeEmployee.objects.create(firstName='Michael', lastName='Patricia', titleName='Dr')
            employee = PartTimeEmployee.objects.create(firstName='Hamza', lastName='Zakaria', titleName='Boxer')
            employee = PartTimeEmployee.objects.create(firstName='Maryam', lastName='Bilal', titleName='Prof')
            employee = PartTimeEmployee.objects.create(firstName='Bilal', lastName='Khalid', titleName='Bowler')
            employee = PartTimeEmployee.objects.create(firstName='Christopher', lastName='Lisa', titleName='Engr')
            employee = PartTimeEmployee.objects.create(firstName='Abderrahman', lastName='Abderrahman', titleName='Referee')
            employee = PartTimeEmployee.objects.create(firstName='William', lastName='Thomas', titleName='Dr')
            employee = PartTimeEmployee.objects.create(firstName='Fatima', lastName='Arwa', titleName='Prof')

    except Exception as e:
        return render(request, 'payrollApp/transaction.html', {'Message':str(e)})
    
    return render(request, 'payrollApp/transaction.html', {'Message': 'Success!'})