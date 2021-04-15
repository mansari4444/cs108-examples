from django.db import models

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

    # maybe add a description of the location
    def __str__(self):
        '''Return a string representation of the make, capacity, and location'''

        return f'{self.make} fits {self.capacity} people exlcuding the crew - {self.location}'
    