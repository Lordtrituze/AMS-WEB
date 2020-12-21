import datetime
import uuid

from django.contrib.auth.decorators import login_required

from app.decorators import unauthenticated_user, allowed_users
from app.models import Passenger
from app.Dto.PassengerDto import *
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from app.service_provider import app_service_provider


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def register_passenger(request):
    context = {
        'title': 'Passenger Registration'
    }
    __create_passenger_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('list_passenger')
    return render(request, 'Passenger/register_passenger.html', context)


def __get_attribute_from_request(register_passenger_dto, request):
    register_passenger_dto.last_name = request.POST['last_name']
    register_passenger_dto.email = request.POST['email']
    register_passenger_dto.address = request.POST['address']
    register_passenger_dto.phone = request.POST['phone']
    register_passenger_dto.username = request.POST['username']
    register_passenger_dto.password = request.POST['password']


def __set_attribute_from_request(request: HttpRequest):
    register_passenger_dto = RegisterPassengerDto()
    register_passenger_dto.first_name = request.POST['first_name']
    __get_attribute_from_request(register_passenger_dto, request)
    return register_passenger_dto


def __create_passenger_if_post_method(request, context):
    if request.method == 'POST':
        try:
            passenger = __set_attribute_from_request(request)
            passenger.reg_no = str(uuid.uuid4()).replace('-', '')[0:10].upper()
            app_service_provider.passenger_management_service().register_passenger(passenger)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e
        return context


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def list_passenger(request):
    passengers = app_service_provider.passenger_management_service().list_passenger()
    context = {
        'passengers': passengers,
        'title': 'Passengers'
    }
    return render(request, 'Passenger/list_passenger.html', context)


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def passenger_details(request, passenger_id: int):
    passenger = app_service_provider.passenger_management_service().passenger_details(passenger_id)
    context = {
        'passenger': passenger,
        'title': 'Passenger Details'
    }
    return render(request, 'Passenger/passenger_details.html', context)


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def edit_passenger(request, passenger_id: int):
    passenger = __get_passenger_or_rise_404(passenger_id)
    context = {
        'passenger': passenger
    }
    # __edit_if_post_method(request, passenger_id, context)
    new_passenger_dto = __edit_if_post_method(request, passenger_id, context)
    if new_passenger_dto is not None:
        context['passenger'] = new_passenger_dto
        if context['saved'] is True:
            return redirect('list_passenger')
    return render(request, 'Passenger/edit_passenger.html', context)


def __get_attribute_from_request_edit(edit_passenger_dto, request):
    edit_passenger_dto.first_name = request.POST['first_name']
    edit_passenger_dto.last_name = request.POST['last_name']
    edit_passenger_dto.email = request.POST['email']
    edit_passenger_dto.address = request.POST['address']
    edit_passenger_dto.phone = request.POST['phone']
    edit_passenger_dto.username = request.POST['username']


def __set_attribute_from_request_edit(request: HttpRequest, aircraft_id):
    edit_aircraft_dto = EditAircraftDto()
    edit_aircraft_dto.aircraft_id = aircraft_id
    __get_attribute_from_request_edit(edit_aircraft_dto, request)
    return edit_aircraft_dto


def __edit_if_post_method(request, aircraft_id: int, context):
    if request.method == 'POST':
        try:
            aircraft = __set_attribute_from_request_edit(request, aircraft_id)
            aircraft.date_updated = datetime.date.today()
            aircraft_service_provider.aircraft_management_service().edit_aircraft(aircraft_id, aircraft)
            context['saved'] = True
            return context
        except Exception as e:
            context['saved'] = False
            raise e


def __get_passenger_or_rise_404(aircraft_id: int):
    try:
        aircraft = aircraft_service_provider.aircraft_management_service().aircraft_details(aircraft_id)
        return aircraft
    except Exception:
        raise Http404('Aircraft Dose Not Exit')


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def delete_aircraft(request, aircraft_id):
    app_service_provider.passenger_management_service().delete_passenger(passenger_id)
    return redirect('list_aircraft')
