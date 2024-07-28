from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'), #home view: can be home view or showmoreMessage view
    path('home', views.Home, name='home'),
    path('index', views.Index, name='index'),
    path('show', views.ShowMoreMessage, name='sm'),
    path('useVariable', views.UseVariableAsResponse, name='uvr'),
    path('getmsg', views.GetRequestVariable, name='GetRequestMessage'),
    path('time', views.DateTimeInfo, name='SDTI'),
    path('logging', views.LoggingExample, name='log'),
    path('iftemp', views.iftemp, name='iftag'),
    path('product', views.ShowProduct, name='product'),
    path('showuser', views.LoadUsers, name='showuser'),
    path('api1', views.CallRestAPI, name='api1'),
    path('api2', views.CallRestAPI2, name='api2'),
    path('showuser2', views.LoadUser2, name='showuser2'),
    path('showuserdetails', views.LoadUserDetails, name='userdetails'),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('author', views.modelTemplate, name= 'authorBook'),
    path('img', views.Static, name='static')
]
