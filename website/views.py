from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # authenticate
        user = authenticate(request, username=username, password=password) # required explicitness because of keyword arguments
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, please try again.')
            return redirect('home')

    else:
        return render(request, 'home.html', {})

# named _user to not conflict with imported methods
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
