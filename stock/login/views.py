from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/portfolio/')
            else:
                messages.info(request, 'Your account is no longer active')
                return redirect('login')
        else:
            messages.info(request, 'Wrong email or password')
            return redirect('login')
    else:
        return render(request, 'login/loginPanel.html', {})

def logout(request):
    auth.logout(request)
    return redirect('/')

def resetPassword(request):
    return render(request, 'resetPassword.html', {})
