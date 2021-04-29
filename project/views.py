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
    model = Boat # retrieve Boat objects from the database
    template_name = "project/home.html" # link to the HTML file that it will use as a format
    context_object_name = "boats" # name (context name) that will refrence this view 

class Specific_boat_PageView(DetailView):
    '''Display a single boat object.'''
    model = Boat  # retrieve Boat objects from the database
    template_name = "project/boat.html" # link to the HTML file that it will use as a format
    context_object_name = "boat" # name (context name) that will refrence this view 

class GuidePageView(DetailView):
    '''Display a single boat object.'''
    model = Guide # retrieve Boat objects from the database
    template_name = "project/guide.html" # link to the HTML file that it will use as a format
    context_object_name = "guide" # name (context name) that will refrence this view 

class BookingPageView(DetailView):
    '''Display a booking'''
    model = Booking # retrieve Boat objects from the database
    template_name = "project/booking.html" # link to the HTML file that it will use as a format
    context_object_name = "booking" # name (context name) that will refrence this view 
    

class CreateBookingView(CreateView):
    '''Create a new booking object and store it in the database.'''
    model = Booking # retrieve Boat objects from the database
    form_class = CreateBookingForm # which form this view links to and uses
    template_name = "project/create_booking_form.html" # link to the HTML file that it will use as a format

class AllBookingPageView(ListView):
    '''Show a list of all bookings.'''
    model = Booking # retrieve Boat objects from the database
    template_name = "project/all_bookings.html" # link to the HTML file that it will use as a format
    context_object_name = "all_bookings" # name (context name) that will refrence this view

class UpdateBookingView(UpdateView):
    '''Update a booking object and store it in the database.'''

    model = Booking # retrieve Boat objects from the database
    form_class = UpdateBookingForm # which form this view links to and uses
    template_name = "project/update_booking_form.html" # link to the HTML file that it will use as a format

class DeleteBookingView(DeleteView):
    '''Delete a booking object and remove it from the database.'''

    template_name = "project/delete_booking_form.html" # link to the HTML file that it will use as a format
    queryset = Booking.objects.all() # which object it should be deleting from in this case its bookings

    def get_success_url(self):
        '''Gives the URL for all bookings once a delete has happened.'''
        return reverse('all_bookings') # this uses "reverse" to obtain the url to all_bookings once the delete happens


class NewCustomerView(CreateView):
    '''Create a new customer for the website.'''
    model = Customer # retrieve Boat objects from the database
    form_class = CreateCustomerForm # which form this view links to and uses
    template_name = "project/create_customer_form.html" # link to the HTML file that it will use as a format

class CustomerView(DetailView):
    '''Shows all the customers bookings.'''
    model = Customer # retrieve Boat objects from the database
    template_name = "project/customer.html" # link to the HTML file that it will use as a format
    context_object_name = "customer"

class AllCustomersView(ListView):
    '''Show all the customers.'''
    model = Customer # retrieve Boat objects from the database
    template_name = "project/all_customers.html" # link to the HTML file that it will use as a format
    context_object_name = "all_customers" # name (context name) that will refrence this view

class AllGuidesView(ListView):
    '''Show all the customers.'''
    model = Guide # retrieve Boat objects from the database
    template_name = "project/all_guides.html" # link to the HTML file that it will use as a format
    context_object_name = "all_guides" # name (context name) that will refrence this view

class DeleteCustomerView(DeleteView):
    '''Delete a customer object and remove it from the database.'''

    template_name = "project/delete_customer_form.html" # link to the HTML file that it will use as a format
    queryset = Customer.objects.all() # which object it should be deleting from in this case its customer

    def get_success_url(self):
        '''Gives the URL for all customers once a delete has happened.'''
        return reverse('all_customers') # this uses "reverse" to obtain the url to all_customers once the delete happens


class NewGuideView(CreateView):
    '''Create a new customer for the website.'''
    model = Guide # retrieve Boat objects from the database
    form_class = CreateGuideForm # which form this view links to and uses
    template_name = "project/create_guide_form.html" # link to the HTML file that it will use as a format


class DeleteGuideView(DeleteView):
    '''Delete a Guide object and remove it from the database.'''

    template_name = "project/delete_guide_form.html" # link to the HTML file that it will use as a format
    queryset = Guide.objects.all() # which object it should be deleting from in this case its guide

    def get_success_url(self):
        '''Gives the URL for all bookings once a delete has happened.'''
        return reverse('all_guides') # this uses "reverse" to obtain the url to all_guides once the delete happens

class NewBoatView(CreateView):
    '''Create a new customer for the website.'''
    model = Boat # retrieve Boat objects from the database
    form_class = CreateBoatForm # which form this view links to and uses
    template_name = "project/create_boat_form.html" # link to the HTML file that it will use as a format

class DeleteBoatView(DeleteView):
    '''Delete a Boat object and remove it from the database.'''

    template_name = "project/delete_boat_form.html" # link to the HTML file that it will use as a format
    queryset = Boat.objects.all() # which object it should be deleting from in this case its boat

    def get_success_url(self):
        '''Gives the URL for all bookings once a delete has happened.'''
        return reverse('home_page') # this uses "reverse" to obtain the url to home_page once the delete happens

class UpdateGuideView(UpdateView):
    '''Update a guide object and store it in the database.'''

    model = Guide # retrieve Boat objects from the database
    form_class = UpdateGuideForm # which form this view links to and uses
    template_name = "project/update_guide_form.html" # link to the HTML file that it will use as a format

class UpdateBoatView(UpdateView):
    '''Update a guide object and store it in the database.'''

    model = Boat # retrieve Boat objects from the database
    form_class = UpdateBoatForm # which form this view links to and uses
    template_name = "project/update_boat_form.html" # link to the HTML file that it will use as a format





