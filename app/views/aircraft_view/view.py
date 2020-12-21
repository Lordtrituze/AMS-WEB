import datetime
import uuid

from django.contrib.auth.decorators import login_required

from app.decorators import unauthenticated_user, allowed_users
from app.models import Aircraft
from app.Dto.AircraftDto import ListAircraftDto, AircraftDetailsDto, EditAircraftDto, RegisterAircraftDto
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from app.service_provider import app_service_provider


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def register_aircraft(request):
    context = {
        'title': 'Aircraft Registration'
    }
    __create_aircraft_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('list_aircraft')
    return render(request, 'Aircraft/register_aircraft.html', context)


def __get_attribute_from_request(register_aircraft_dto, request):
    register_aircraft_dto.aircraft_type = request.POST['aircraft_type']
    register_aircraft_dto.aircraft_capacity = request.POST['aircraft_capacity']


def __set_attribute_from_request(request: HttpRequest):
    register_aircraft_dto = RegisterAircraftDto()
    register_aircraft_dto.aircraft_name = request.POST['aircraft_name']
    __get_attribute_from_request(register_aircraft_dto, request)
    return register_aircraft_dto


def __create_aircraft_if_post_method(request, context):
    if request.method == 'POST':
        try:
            aircraft = __set_attribute_from_request(request)
            aircraft.aircraft_no = str(uuid.uuid4()).replace('-', '')[0:10].upper()
            aircraft.date_created = datetime.date.today()
            app_service_provider.aircraft_management_service().register_aircraft(aircraft)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e
        return context


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def list_aircraft(request):
    aircrafts = app_service_provider.aircraft_management_service().list_aircraft()
    context = {
        'aircrafts': aircrafts,
        'title': 'Aircrafts'
    }
    return render(request, 'Aircraft/list_aircraft.html', context)


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def aircraft_details(request, aircraft_id: int):
    aircraft = app_service_provider.aircraft_management_service().aircraft_details(aircraft_id)
    context = {
        'aircraft': aircraft,
        'title': 'Aircraft Details'
    }
    return render(request, 'Aircraft/aircraft_details.html', context)


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def edit_aircraft(request, aircraft_id: int):
    aircraft = __get_aircraft_or_rise_404(aircraft_id)
    context = {
        'aircraft': aircraft
    }
    __edit_if_post_method(request, aircraft_id, context)
    new_aircraft_dto = __edit_if_post_method(request, aircraft_id, context)
    if new_aircraft_dto is not None:
        context['aircraft'] = new_aircraft_dto
        if context['saved'] is True:
            return redirect('list_aircraft')
    return render(request, 'Aircraft/edit_aircraft.html', context)


def __get_attribute_from_request_edit(edit_aircraft_dto, request):
    edit_aircraft_dto.aircraft_type = request.POST['aircraft_type']
    edit_aircraft_dto.aircraft_name = request.POST['aircraft_name']
    edit_aircraft_dto.aircraft_capacity = request.POST['aircraft_capacity']


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
            app_service_provider.aircraft_management_service().edit_aircraft(aircraft_id, aircraft)
            context['saved'] = True
            return context
        except Exception as e:
            context['saved'] = False
            raise e


def __get_aircraft_or_rise_404(aircraft_id: int):
    try:
        aircraft = app_service_provider.aircraft_management_service().aircraft_details(aircraft_id)
        return aircraft
    except Exception:
        raise Http404('Aircraft Dose Not Exit')


@login_required(login_url='login_get')
@allowed_users(['staffs'])
def delete_aircraft(request, aircraft_id):
    app_service_provider.aircraft_management_service().delete_aircraft(aircraft_id)
    return redirect('list_aircraft')
