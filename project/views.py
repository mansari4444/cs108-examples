from django.shortcuts import render, redirect
from django.views.generic import *
from django.views.generic.edit import *
from django.urls import reverse
from .forms import *
from .models import *
from django import forms
# from django import forms
import random
# Create your views here.

class HomePageView(ListView):
    '''Show a list of boats available and locations they service.'''
    model = Boat # retrieve Boat objects from the databse
    template_name = "project/home.html"
    context_object_name = "boats"

class Specific_boat_PageView(DetailView):
    '''Display a single boat object.'''
    model = Boat  # retrieve Boat objects from the databse
    template_name = "project/boat.html"
    context_object_name = "boat"

class GuidePageView(DetailView):
    '''Display a single boat object.'''
    model = Guide # retrieve Boat objects from the databse
    template_name = "project/guide.html"
    context_object_name = "guide"

class BookingPageView(DetailView):
    '''Display a booking'''
    model = Booking
    template_name = "project/booking.html"
    context_object_name = "booking"
    

class CreateBookingView(CreateView):
    '''Create a new booking object and store it in the database.'''
    model = Booking
    form_class = CreateBookingForm
    template_name = "project/create_booking_form.html"

class AllBookingPageView(ListView):
    '''Show a list of all bookings.'''
    model = Booking # retrieve Boat objects from the databse
    template_name = "project/all_bookings.html"
    context_object_name = "all_bookings"

class UpdateBookingView(UpdateView):
    '''Update a booking object and store it in the database.'''

    model = Booking # which model to create
    form_class = UpdateBookingForm
    template_name = "project/update_booking_form.html"

class DeleteBookingView(DeleteView):
    '''Delete a booking object and remove it from the database.'''

    template_name = "project/delete_booking_form.html"
    queryset = Booking.objects.all()

    def get_success_url(self):
        '''Gives the URL for all bookings once a delete has happened.'''
        return reverse('all_bookings')


class NewCustomerView(CreateView):
    '''Create a new customer for the website.'''
    model = Customer
    form_class = CreateCustomerForm
    template_name = "project/create_customer_form.html"

class CustomerView(DetailView):
    '''Shows all the customers bookings.'''
    model = Customer
    template_name = "project/customer.html"
    context_object_name = "customer"

class AllCustomersView(ListView):
    '''Show all the customers.'''
    model = Customer # retrieve Boat objects from the databse
    template_name = "project/all_customers.html"
    context_object_name = "all_customers"

class AllGuidesView(ListView):
    '''Show all the customers.'''
    model = Guide # retrieve Boat objects from the databse
    template_name = "project/all_guides.html"
    context_object_name = "all_guides"

class DeleteCustomerView(DeleteView):
    '''Delete a customer object and remove it from the database.'''

    template_name = "project/delete_customer_form.html"
    queryset = Customer.objects.all()

    def get_success_url(self):
        '''Gives the URL for all bookings once a delete has happened.'''
        return reverse('all_customers')


class NewGuideView(CreateView):
    '''Create a new customer for the website.'''
    model = Guide
    form_class = CreateGuideForm
    template_name = "project/create_guide_form.html"


class DeleteGuideView(DeleteView):
    '''Delete a Guide object and remove it from the database.'''

    template_name = "project/delete_guide_form.html"
    queryset = Guide.objects.all()

    def get_success_url(self):
        '''Gives the URL for all bookings once a delete has happened.'''
        return reverse('all_guides')

class NewBoatView(CreateView):
    '''Create a new customer for the website.'''
    model = Boat
    form_class = CreateBoatForm
    template_name = "project/create_boat_form.html"

class DeleteBoatView(DeleteView):
    '''Delete a Boat object and remove it from the database.'''

    template_name = "project/delete_boat_form.html"
    queryset = Boat.objects.all()

    def get_success_url(self):
        '''Gives the URL for all bookings once a delete has happened.'''
        return reverse('home_page')

class UpdateGuideView(UpdateView):
    '''Update a guide object and store it in the database.'''

    model = Guide # which model to create
    form_class = UpdateGuideForm
    template_name = "project/update_guide_form.html"

class UpdateBoatView(UpdateView):
    '''Update a guide object and store it in the database.'''

    model = Boat # which model to create
    form_class = UpdateBoatForm
    template_name = "project/update_boat_form.html"





