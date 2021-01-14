from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from app.decorators import unauthenticated_user


# @unauthenticated_user
def login_page_post(request):
    context = {}
    username = request.POST.get('username', False)
    password = request.POST.get('password')
    user: User = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.groups.filter(name__exact="staffs").exists():
            return redirect("register_aircraft")
        elif user.groups.filter(name__exact="passengers").exists():
            return redirect("register_passenger")
    else:
        context['message'] = 'username or password incorrect'
    return render(request, 'login.html', context)


@unauthenticated_user
def login_get(request):
    context = {}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home_page')


def home_page(request):
    context = {}
    return render(request, 'Home.html', context)
