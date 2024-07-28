from django.urls import path
from formApp import views

urlpatterns = [
    path('signup/', views.SignUp, name='signup')
]