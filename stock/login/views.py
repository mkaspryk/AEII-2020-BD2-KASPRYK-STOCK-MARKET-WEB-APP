from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if username=="" or first_name=="" or last_name=="" or email =="" or password1=="" or password2=="":
            messages.info(request,'You have to fill all fields !')
            return redirect('register')
        else:
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username is taken !')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email is already used !')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                    user.save()

            else:
                messages.info(request,'Password not matching !')
                return redirect('register')
            user = auth.authenticate(username=username,password=password1)
            auth.login(request,user)
            return redirect('/welcome')
    else:
        return render(request, 'register/registerPanel.html',{})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/portfolio')
            else:
                messages.info(request,'Your account is no longer active')
                return redirect('login')
        else:
            messages.info(request,'Wrong email or password')
            return redirect('login')
    else:
        return render(request, 'login/loginPanel.html',{})

def logout(request):
    auth.logout(request)
    return redirect('/')

def resetPassword(request):
    return render(request, 'resetPassword.html', {})