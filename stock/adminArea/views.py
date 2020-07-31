
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import time

# Create your views here.

def adminArea(request):
    username = request.POST['username']
    user = User.objects.get(username=username)
    if(user.is_superuser==true)
	    return render(request, 'adminArea.html', {})
    else:
        return render(request, 'AccessDenied.html',{})

def set_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        user = User.objects.get(username=username)
        user.is_superuser = True
        user.save()
        return render(request, 'set_admin.html',{})
    else:
        return render(request, 'set_admin.html',{})

def remove_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        user = User.objects.get(username=username)
        user.is_superuser = False
        user.save()
        return render(request, 'remove_admin.html',{})
    else:
        return render(request, 'remove_admin.html',{})

def ban_hammer(request):
    if request.method == "POST":
        username = request.POST['username']
        user = User.objects.get(username=username)
        user.is_active = False
        user.save()
        return render(request, 'ban_hammer.html',{})
    else:
        return render(request, 'ban_hammer.html',{})

def unban(request):
    if request.method == "POST":
        username = request.POST['username']
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        return render(request, 'unban.html',{})
    else:
        return render(request, 'unban.html',{})
