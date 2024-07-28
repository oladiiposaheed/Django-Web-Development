from django.urls import path
from chartApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chart/<str:chart_type>/', views.get_chart_data, name='get_chart_data')
]
