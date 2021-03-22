from django.db import models
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    '''MiniFacebook model'''

    # data attributes:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def get_status_messages(self):
        '''Takes profile messages for the Person'''

        return StatusMessage.objects.filter(profile=self)
    

    def __str__(self):
        '''Return a string representation of the name and city'''

        return f'{self.first_name} {self.last_name} - {self.city}'

class StatusMessage(models.Model):
    '''Data attributes of facebook status message'''

    # data attributes:
    timestamp = models.TimeField(blank=True, auto_now=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of the StatusMessage'''

        return f'{self.timestamp}  {self.message}'
        
