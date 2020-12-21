from django.urls import path
from app.views.staff_view import view

urlpatterns = [
    path('home/', view.staff_home, name='staff_home'),

]
