from django.shortcuts import render

# Create your views here.
def home(request):
    templatefilename = 'basicApp2/home.html'
    return render(request, templatefilename)