from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm


def signup_view(request):
    signup_form = SignupForm(request.POST or None)
    if signup_form.is_valid():
        signup_form.save()
        username = signup_form.cleaned_data.get('username')
        messages.success(
            request, f'Account successfully created for {username}, please login!')
        return redirect('users:login')
    return render(request, 'users/sign_up.html', context={'form': signup_form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = authenticate(username=username,
                                password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                messages.success(
                    request, f'You have been successfully logged in as {username}')
                return redirect('blog:home')
            else:
                messages.error(
                    request, 'There was an error in your password and email!')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', context={
        'form': form
    })


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out!')
    return redirect('users:login')
