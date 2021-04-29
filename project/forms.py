#forms.py

from django import forms
from .models import *

class CreateBookingForm(forms.ModelForm):
    '''A form to create a new booking.'''

    
    date_of_booking = forms.DateField()

    class Meta:
        '''additional data about this form'''
        model = Booking #which model to create
        fields = ['boat','customer', 'guide','date_of_booking']# which fields to create

class UpdateBookingForm(forms.ModelForm):
    '''A form to update booking object.'''

    class Meta:
        '''additional data about this form'''
        model = Booking # which model to create
        fields = ['boat','customer', 'guide','date_of_booking'] # which fields to create


class CreateCustomerForm(forms.ModelForm):
    '''A form to create a new customer object and store it in the database.'''

    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.CharField()
    email = forms.CharField()
    date_of_birth = forms.DateField()

    class Meta:
        '''additional data about this form'''
        model = Customer 
        fields = ['first_name','last_name', 'address','email', 'date_of_birth']# which fields to create

class CreateGuideForm(forms.ModelForm):
    '''A form to create a new guide.'''

    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.CharField()
    email = forms.CharField()
    date_of_birth = forms.DateField()
    years_of_experience = forms.IntegerField()
    image_url = forms.URLField()

    class Meta:
        '''additional data about this form'''
        model = Guide 
        fields = ['first_name','last_name', 'address','email', 'date_of_birth', 'years_of_experience', 'image_url']# which fields to create


class CreateBoatForm(forms.ModelForm):
    '''A form to create a new boat object.'''

    
    Boat_identification_number = forms.CharField()
    make = forms.CharField()
    capacity = forms.IntegerField()
    price_per_person = forms.IntegerField()
    location = forms.CharField()
    image_url = forms.URLField()
    Location_description = forms.CharField()
    location_image_url = forms.URLField()

    class Meta:
        '''additional data about this form'''
        model = Boat #which model to create
        fields = ['Boat_identification_number','make', 'capacity','price_per_person', 'location', 'image_url', 'Location_description', 'location_image_url']# which fields to create


class UpdateGuideForm(forms.ModelForm):
    '''A form to update guide object.'''

    class Meta:
        '''additional data about this form'''
        model = Guide # which model to create
        fields = ['first_name','last_name', 'address','email', 'date_of_birth', 'years_of_experience', 'image_url'] # which fields to create

class UpdateBoatForm(forms.ModelForm):
    '''A form to update boat object.'''

    class Meta:
        '''additional data about this form'''
        model = Boat # which model to create
        fields = ['Boat_identification_number','make', 'capacity','price_per_person', 'location', 'image_url', 'Location_description', 'location_image_url'] # which fields to create




   
