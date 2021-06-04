from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    context_dict = {}

    return render(request, 'dynamica_app/index.html', context_dict)

def user_login(request):
    # Define the context dictionary with an empty error message
    context_dict = {'error_message': None}

    # If the method is POST (form has been submitted) the form will be processed
    if request.method == 'POST':
        # Get the username and password values from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Attempt to authenticate the user with the provided details
        user = authenticate(username=username, password=password)

        # If a user with the given username and password exists
        if user:
            # Check that their account is still active
            # If it is then log the user in
            if user.is_active:
                login(request, user)

                # Redirect the user back to the home page
                return redirect(reverse('menu'))

            # If the account exists but is disabled, display an error message
            else:
                context_dict['error_message'] = "Account is disabled"

        # If an account with the given details does not exist, display an error message
        else:
            context_dict['error_message'] = "Username or Password is incorrect"

    # If the form has not been submitted, render the view onscreen
    return render(request, 'dynamica_app/login.html', context=context_dict)

@login_required
def menu(request):
    context_dict = {}

    return render(request, 'dynamica_app/landing.html', context=context_dict)

@login_required
def user_logout(request):
    # Log the user out
    logout(request)

    # Redirect the user back to the home page
    return redirect(reverse('index'))
