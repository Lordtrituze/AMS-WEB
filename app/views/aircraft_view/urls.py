from django.urls import path
from app.views.aircraft_view import view

urlpatterns = [
    path('register/', view.register_aircraft, name='register_aircraft'),
    path('list/', view.list_aircraft, name='list_aircraft'),
    path('details/<int:aircraft_id>/', view.aircraft_details, name='aircraft_details'),
    path('edit/<int:aircraft_id>/', view.edit_aircraft, name='edit_aircraft'),
    path('delete/<int:aircraft_id>/', view.delete_aircraft, name='delete_aircraft'),
]