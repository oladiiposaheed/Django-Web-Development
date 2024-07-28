from django.urls import path
from payrollApp import views

urlpatterns = [
    path('employeelist', views.employeeList, name='employeelist'),
    path('employeedetails/<int:id>', views.employeeDetails, name='employeedetails'),
    path('employeedelete/<int:id>', views.employeeDelete, name='employeedelete'),
    path('employeeupdate/<int:id>', views.employeeUpdate, name='employeeupdate'),
    path('employeeinsert', views.employeeInsert, name='employeeinsert'),
    path('employeeparttime', views.BulkInsert, name='employeeparttime'),
    path('newbulkinsert', views.NewBulkInsert, name='newbulkinsert'),
    path('bulkupdate', views.BulkUpdate, name='bulkupdate'),
    path('bulkdelete', views.BulkDelete, name='bulkdelete'),
    path('employeepage', views.PageEmployeeList, name='employeepage'),
    path('cascade', views.cascadingSelect, name='cascade'),
    path('state', views.load_state, name='state'),
    path('city', views.load_city, name='city'),
    path('transaction', views.Transaction, name='transaction')
]


