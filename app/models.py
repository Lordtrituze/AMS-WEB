import datetime

from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.


class Aircraft(models.Model):
    aircraft_name = models.CharField(max_length=20)
    aircraft_type = models.CharField(max_length=20)
    aircraft_capacity = models.IntegerField(max_length=None)
    aircraft_no = models.CharField(max_length=15)
    date_created = models.DateField(default=datetime.date.today)
    date_updated = models.DateField(null=True)

    def __str__(self):
        return f"{self.aircraft_name:<15}\t{self.aircraft_type:<15}\t{self.aircraft_capacity:<10}\t{self.aircraft_no:<15}\t{self.date_created:<20}\t{self.date_updated}"


class Passenger(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    reg_no = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name:<20}\t{self.last_name:<20}\t{self.email:<25}\t{self.phone:<20}\t{self.address:<25}\t{self.reg_no}"


class Flight(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.RESTRICT)
    takeoff_location = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    departure_date = models.DateField()
    arrival_time = models.TimeField()
    flight_number = models.CharField(max_length=15)
    price = models.FloatField()
    date_created = models.DateField(default=datetime.date.today)
    date_updated = models.DateField(null=True)

    def __str__(self):
        return f"{self.aircraft:<5}\t{self.takeoff_location:<15}\t{self.destination:<15}\t{self.departure_date:<15}\t{self.arrival_time:<15}\t{self.fl}"


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.RESTRICT)
    passenger = models.ForeignKey(Passenger, on_delete=models.RESTRICT)
    flight_class = models.CharField(max_length=20)
    price = models.FloatField()
    booking_reference = models.UUIDField(default=uuid.uuid4())


class Staff(models.Model):
    role = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    date_of_employment = models.DateField(default=datetime.date.today)
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
