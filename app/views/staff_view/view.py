from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.decorators import unauthenticated_user, allowed_users
from app.service_provider import app_service_provider


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def list_staffs(request):
    staffs = app_service_provider.staff_management_service().list_staff()
    context = {
        'staffs': staffs
    }
    return render(request, '', context)


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def staff_home(request):
    context = {'message': 'Welcome!'}

    return render(request, 'Staff/home_view.html', context)
