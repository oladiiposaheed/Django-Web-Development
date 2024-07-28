from django.shortcuts import render

# Create your views here.

def home(request):
    templatefilename = 'basicApp1/home.html'
    return render(request, templatefilename)