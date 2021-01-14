from django.urls import path
from app.views.flight_view import view

urlpatterns = [
    path('home/', view.home, name='home'),
    path('register/', view.register_flight, name='register_flight'),
    path('list/', view.list_flight, name='list_flight'),
    path('details/<int:flight_id>/', view.flight_details, name='flight_details'),
    path('edit/<int:flight_id>/', view.edit_flight, name='edit_flight'),
    path('delete/<int:flight_id>/', view.delete_flight, name='delete_flight'),
    path('search/', view.search_flight, name='search_flight'),
]