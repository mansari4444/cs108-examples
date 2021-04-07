from django.db import models
from django.urls import reverse 
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
    friends = models.ManyToManyField("self")

    def get_status_messages(self):
        '''Takes profile messages for the Person'''

        return StatusMessage.objects.filter(profile=self)
    

    def __str__(self):
        '''Return a string representation of the name and city'''

        return f'{self.first_name} {self.last_name} - {self.city}'
    
    def get_absolute_url(self):
        '''Provide a URL to show this object'''

        return reverse('show_profile_page', kwargs={'pk':self.pk})

    def get_friends(self):
        '''Returns all friends for this profile.'''

        return Profile.objects.filter(friends=self.pk)

    def get_news_feed(self):
        '''Obtain and return news feed items.'''

        news = StatusMessage.objects.all().order_by("-timestamp")

        friends = self.get_friends()

        friends_news = news.filter(profile__in=friends)

        self_news = news.filter(profile=self.pk)

        total = self_news | friends_news

        return total

    def get_friend_suggestions(self):
        '''Potential friends that can be added'''

        possible_friends = friend_suggestions = Profile.objects.exclude(pk__in=self.get_friends()).exclude(pk=self.pk)

        return possible_friends
        
class StatusMessage(models.Model):
    '''Data attributes of facebook status message'''

    # data attributes:
    timestamp = models.TimeField(blank=True, auto_now=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(blank=True) # an actual image
    def __str__(self):
        '''Return a string representation of the StatusMessage'''

        return f'{self.timestamp}  {self.message}'

        
