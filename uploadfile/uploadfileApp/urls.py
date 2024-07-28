from django.urls import path
from uploadfileApp import views
urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/create', views.employee_create, name='employee_create'),
    path('employee/list', views.employee_list, name='employee_list'),
    path('employee/details/<int:employee_id>/', views.employee_details, name='employee_details'),
]

