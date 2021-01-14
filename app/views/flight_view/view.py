import datetime
import uuid

from app.Dto.FlightDto import EditFlightDto, RegisterFlightDto
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from app.service_provider import app_service_provider


def home(request):
    context ={
        'title': 'Home'
    }
    return render(request, 'Flight/base.html', context)


def register_flight(request):
    aircrafts = app_service_provider.aircraft_management_service().get_aircraft_list()
    context = {
        'title': 'Flight Registration',
        'aircrafts': aircrafts
    }
    __create_flight_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('list_flight')
    return render(request, 'Flight/register_flight.html', context)


def __get_attribute_from_request(register_flight_dto, request):
    register_flight_dto.takeoff_location = request.POST.get('takeoff_location')
    register_flight_dto.destination = request.POST['destination']
    register_flight_dto.departure_date = request.POST['departure_date']
    register_flight_dto.arrival_time = request.POST['arrival_time']
    register_flight_dto.price = request.POST['price']


def __set_attribute_from_request(request: HttpRequest):
    register_flight_dto = RegisterFlightDto()
    register_flight_dto.aircraft_id = request.POST['aircraft_id']
    __get_attribute_from_request(register_flight_dto, request)
    return register_flight_dto


def __create_flight_if_post_method(request, context):
    if request.method == 'POST':
        try:
            flight = __set_attribute_from_request(request)
            flight.flight_number = str(uuid.uuid4()).replace('-', '')[0:10].upper()
            flight.date_created = datetime.date.today()
            app_service_provider.flight_management_service().register_flight(flight)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e
        return context


def list_flight(request):
    flights = app_service_provider.flight_management_service().list_flight()
    context = {
        'flights': flights,
        'title': 'Flights'
    }
    return render(request, 'Flight/list_flight.html', context)


def flight_details(request, flight_id: int):
    flight = app_service_provider.flight_management_service().flight_details(flight_id)
    context = {
        'flight': flight,
        'title': 'Flight Details'
    }
    return render(request, 'Flight/flight_details.html', context)


def edit_flight(request, flight_id: int):
    flight = __get_flight_or_rise_404(flight_id)
    aircrafts = app_service_provider.aircraft_management_service().get_aircraft_list()
    context = {
        'flight': flight,
        'aircrafts': aircrafts
    }
    __edit_if_post_method(request, flight_id, context)
    new_flight_dto = __edit_if_post_method(request, flight_id, context)
    if new_flight_dto is not None:
        context['aircraft'] = new_flight_dto
        if context['saved'] is True:
            return redirect('list_flight')
    return render(request, 'Flight/edit_flight.html', context)


def __get_attribute_from_request_edit(flight_id: int, request: HttpRequest, ) -> EditFlightDto:
    edit_flight_dto = EditFlightDto()
    edit_flight_dto.flight_id = flight_id
    __set_attribute_from_request_edit(edit_flight_dto, request)
    return edit_flight_dto


def __set_attribute_from_request_edit(edit_flight_dto, request):
    edit_flight_dto.takeoff_location = request.POST['takeoff_location']
    edit_flight_dto.destination = request.POST['destination']
    edit_flight_dto.departure_date = request.POST['departure_date']
    edit_flight_dto.arrival_time = request.POST['arrival_time']
    edit_flight_dto.price = request.POST['price']
    edit_flight_dto.aircraft_id = request.POST['aircraft_id']


def __edit_if_post_method(request, flight_id: int, context):
    if request.method == 'POST':
        try:
            flight = __get_attribute_from_request_edit(flight_id, request)
            flight.date_updated = datetime.date.today()
            app_service_provider.flight_management_service().edit_flight(flight_id, flight)
            context['saved'] = True
            return context
        except Exception as e:
            context['saved'] = False
            raise e


def __get_flight_or_rise_404(flight_id: int):
    try:
        flight = app_service_provider.flight_management_service().flight_details(flight_id)
        return flight
    except Exception:
        raise Http404('Flight Dose Not Exit')


def delete_flight(request, flight_id: int):
    app_service_provider.flight_management_service().delete_flight(flight_id)
    return redirect('list_flight')


def search_flight(request):
    takeoff_location = request.POST.get('takeoff_location', False)
    departure_date = request.POST.get('departure_date', '')
    destination = request.POST.get('destination', False)
    flights = app_service_provider.flight_management_service().search_flight(takeoff_location, destination,
                                                 departure_date)
    context = {
        'flights': flights
    }
    return render(request, 'Flight/search_flight.html', context)
