import uuid
from app.Dto.PassengerDto import *
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from app.service_provider import app_service_provider
from secrets import compare_digest


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
    register_passenger_dto.confirm_password = request.POST['confirm_password']


def __set_attribute_from_request(request: HttpRequest):
    register_passenger_dto = RegisterPassengerDto()
    register_passenger_dto.first_name = request.POST['first_name']
    __get_attribute_from_request(register_passenger_dto, request)
    return register_passenger_dto


def __create_passenger_if_post_method(request, context):
    if request.method == 'POST':
        try:
            passenger = __set_attribute_from_request(request)
            if compare_digest(passenger.password, passenger.confirm_password):
                passenger.reg_no = str(uuid.uuid4()).replace('-', '')[0:10].upper()
                app_service_provider.passenger_management_service().register_passenger(passenger)
                context['saved'] = True
            else:
                context['message'] = 'passwords do not match'
                context['saved'] = False
        except Exception as e:
            context['saved'] = False
            raise e
        return context


def list_passenger(request):
    passengers = app_service_provider.passenger_management_service().list_passenger()
    context = {
        'passengers': passengers,
        'title': 'Passengers'
    }
    return render(request, 'Passenger/list_passenger.html', context)


def passenger_details(request, passenger_id: int):
    passenger = app_service_provider.passenger_management_service().passenger_details(passenger_id)
    context = {
        'passenger': passenger,
        'title': 'Passenger Details'
    }
    return render(request, 'Passenger/passenger_details.html', context)


def edit_passenger(request, passenger_id: int):
    passenger = __get_passenger_or_rise_404(passenger_id)
    context = {
        'passenger': passenger

    }
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


def __set_attribute_from_request_edit(request: HttpRequest, passenger_id):
    edit_passenger_dto = EditPassengerDto()
    edit_passenger_dto.passenger_id = passenger_id
    edit_passenger_dto.first_name = request.POST['first_name']
    __get_attribute_from_request_edit(edit_passenger_dto, request)
    return edit_passenger_dto


def __edit_if_post_method(request, passenger_id: int, context):
    if request.method == 'POST':
        try:
            passenger = __set_attribute_from_request_edit(request, passenger_id)
            app_service_provider.passenger_management_service().edit_passenger(passenger_id, passenger)
            context['saved'] = True
            return context
        except Exception as e:
            context['saved'] = False
            raise e


def __get_passenger_or_rise_404(passenger_id: int):
    try:
        passenger = app_service_provider.passenger_management_service().passenger_details(passenger_id)
        return passenger
    except Exception:
        raise Http404('Aircraft Dose Not Exit')


def delete_passenger(request, passenger_id):
    app_service_provider.passenger_management_service().delete_passenger(passenger_id)
    return redirect('list_passenger')


def passenger_home(request):
    return render(request, 'Passenger/passenger_home.html')
