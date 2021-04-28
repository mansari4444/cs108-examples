from django.db import models
from django.urls import reverse 
from django.utils import timezone

# Create your models here.

class Boat(models.Model):
    '''Represents a boat which a seat can be booked on.'''

    # data attributes:
    Boat_identification_number = models.TextField(blank=True)
    make = models.TextField(blank=True)
    capacity = models.IntegerField(blank=False)
    price_per_person = models.IntegerField(blank=False)
    location = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    Location_description = models.TextField(blank=True)
    
    def __str__(self):
        '''Return a string representation of the make, capacity, and location'''

        return f'{self.make} fits {self.capacity} people exlcuding the crew - {self.location}'
    
    def get_absolute_url(self):
        '''Provide a URL to show this object'''

        return reverse('boat', kwargs={'pk':self.pk})
    
class Customer(models.Model):
    '''Represents a customer.'''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    address = models.TextField(blank=True)
    email = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True)

    def __str__(self):
        '''Return a string representation of the make, capacity, and location'''

        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        '''Provide a URL to show this object'''

        return reverse('customer', kwargs={'pk':self.pk})

class Guide(models.Model):
    '''Represents qualified guide for the expedition.'''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    address = models.TextField(blank=True)
    email = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True)
    years_of_experience = models.IntegerField(blank=False)
    image_url = models.URLField(blank=True)
    

    
    def __str__(self):
        '''Return a string representation of the make, capacity, and location'''

        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        '''Provide a URL to show this object'''

        return reverse('guide', kwargs={'pk':self.pk})

class Booking(models.Model):
    '''Entails the booking of a customer.'''
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True, blank=True)
    date_of_booking = models.DateField(blank=True, null=True)
    total_price = models.IntegerField(blank=False, null=True)

    def __str__(self):
        '''Return a string representation of the make, capacity, and location'''

        return f'{self.customer}, Price: ${self.total_price}, Date of booking: {self.date_of_booking}, Booking details: {self.boat}'

    def get_absolute_url(self):
        '''Provide a URL to show this object'''

        return reverse('booking', kwargs={'pk':self.pk})



