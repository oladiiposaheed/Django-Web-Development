from django.shortcuts import render
from formApp.forms import UserRegistrationForm
# Create your views here.

def SignUp(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #form.save()
            return render(request, 'formApp/homepage.html')
        
    else:
        form = UserRegistrationForm()
    return render(request, 'formApp/signUp.html', {'form': form})