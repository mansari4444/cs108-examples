from django.db import models

# Create your models here.

class Profile(models.Model):
    '''MiniFacebook model'''

    # data attributes:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    

    def __str__(self):
        '''Return a string representation of the name and city'''

        return f'{self.first_name} {self.last_name} - {self.city}'
