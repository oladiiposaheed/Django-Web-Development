from django.urls import path
from authApp import views

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('change_pwd', views.change_password, name='change_pwd'),
    path('change_profile', views.change_profile, name='change_profile'),
    path('delete_account', views.delete_account, name='delete_account'),
    path('signout', views.signout, name='signout'),
]
