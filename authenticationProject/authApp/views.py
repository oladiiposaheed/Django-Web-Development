from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from authApp.forms import SignUpForm, ChangeProfileForm
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signUp(request):
    #form = UserCreationForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('home') #Redirect to home page

    else:
        form = SignUpForm()
    dict = {'form': form}
    return render(request, 'authApp/signup.html', dict)

@login_required
def home(request):
    return render(request, 'authApp/home.html')

def login_view(request):
    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    dict = {'form': form}
    return render(request, 'authApp/login.html', dict)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #To maintain the session
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
        
    dict = {'form': form}
    return render(request, 'authApp/change_pwd.html', dict)


@login_required
def change_profile(request):
    #form = UserChangeForm(instance=request.user)
    if request.method == 'POST':
        form = ChangeProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ChangeProfileForm(instance=request.user)
    dict = {'form': form}
    return render(request, 'authApp/change_profile.html', dict)

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('login') # Redirect to signup after account deletion
    
    return render(request, 'authApp/delete_account.html')

@login_required
def signout(request):
    logout(request)
    return redirect('login') 