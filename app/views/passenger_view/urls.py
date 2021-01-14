from django.urls import path
from app.views.passenger_view import view

urlpatterns = [
    path('register/', view.register_passenger, name="register_passenger"),
    path('list/', view.list_passenger, name="list_passenger"),
    path('edit/<int:passenger_id>/', view.edit_passenger, name="edit_passenger"),
    path('details/<int:passenger_id>/', view.passenger_details, name="passenger_details"),
    path('delete/<int:passenger_id>/', view.delete_passenger, name="delete_passenger"),
    path('home/', view.passenger_home, name='passenger_home')
]