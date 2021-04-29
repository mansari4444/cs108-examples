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
    image_url = models.URLField(blank=True) # a location of the picture of how the boat looks like
    Location_description = models.TextField(blank=True)
    location_image_url = models.URLField(blank=True) # a link to an image of the location the diving will happen at
    
    def __str__(self):
        '''Return a string representation of the make, capacity, and location'''

        return f'{self.make} fits {self.capacity} people exlcuding the crew - {self.location}'
        # returns a string 
    
    def get_absolute_url(self):
        '''Provide a URL to show this object'''

        return reverse('boat', kwargs={'pk':self.pk})
        # provides a return url for the delete function
    
class Customer(models.Model):
    '''Represents a customer.'''
    # data attributes:
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
        # provides a return url for the delete function

class Guide(models.Model):
    '''Represents qualified guide for the expedition.'''
    # data attributes:
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
        # provides a return url for the delete function

class Booking(models.Model):
    '''Entails the booking of a customer.'''
    # data attributes:
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, null=True, blank=True) # this links booking to Boat class using a foreign key it is set to null=true to not allow errors to come up if not filled in
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True) # this links booking to Customer class using a foreign key it is set to null=true to not allow errors to come up if not filled in
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True, blank=True) # this links booking to Guide class using a foreign key it is set to null=true to not allow errors to come up if not filled in
    date_of_booking = models.DateField(blank=True, null=True) # attribute of Booking and uses a DateField to be able to format dates inputted
   

    def __str__(self):
        '''Return a string representation of the make, capacity, and location'''

        return f'{self.customer}, Price: ${self.total_price}, Date of booking: {self.date_of_booking}, Booking details: {self.boat}'

    def get_absolute_url(self):
        '''Provide a URL to show this object'''

        return reverse('booking', kwargs={'pk':self.pk})
        # provides a return url for the delete function



