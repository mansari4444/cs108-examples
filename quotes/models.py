from django.db import models
from django.urls import reverse
import random

# Create your models here.

class Person(models.Model):
    '''Represent a person who said something noteable'''

    name = models.TextField(blank=True)

    def __str__(self):
        '''Return a string representation of this person'''
        return self.name

    def get_random_image(self):
        '''Return an image of this person, selected at random'''
        # find all images for this person:
        images = Image.objects.filter(person=self)

        # select one at random to return
        return random.choice(images)

    def get_all_quotes(self):
        '''Return all quotes for this person'''

        # use the object manager to filter Quotes by this persons PK:
        return Quote.objects.filter(person=self)
    
    def get_all_images(self):
        '''Return all images for this person'''

        # use the object manager to filter Images by this persons PK:
        return Image.objects.filter(person=self)



class Quote(models.Model):
    '''Represents a quote by a famous person'''

    # data attirbutes:
    text = models.TextField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # author = models.TextField(blank=True)
    # image_url = models.URLField(blank=True)
    

    def __str__(self):
        '''Return a string representation of this quote'''

        return f'"{self.text} - {self.person}"'
    
    def get_absolute_url(self):
        '''Provide a url to show this object'''

        # 'quote/<int:pk>'
        return reverse('quote', kwargs={'pk':self.pk})

class Image(models.Model):
    '''Represent an image URL for a person.'''

    image_url = models.URLField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
 
    def __str__(self):
        '''Return the image url of this image'''
        return self.image_url