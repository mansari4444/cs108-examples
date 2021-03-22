from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quote, Person
import random

class HomePageView(ListView):
    '''Show a listing of quotes'''
    model = Quote # retrieve Quote objects from the database
    template_name = "quotes/home.html"
    context_object_name = "quotes"

class QuotePageView(DetailView):
    '''Display a single quote object.'''
    model = Quote # retrieve Quote objects from the database
    template_name = "quotes/quote.html" # delegate the display to this template
    context_object_name = "quote" # use this variable name in the template

class RandomQuotePageView(DetailView):
    '''Display a single quote object.'''
    model = Quote # retrieve Quote objects from the database
    template_name = "quotes/quote.html" # delegate the display to this template
    context_object_name = "quote" # use this variable name in the template

    def get_object(self):
        '''Select one quote at random for display in the quote.html template'''

        # obtain all quotes using the object manager
        quotes = Quote.objects.all()
        # select one at random
        q = random.choice(quotes)
        return q

class PersonPageView(DetailView):
    '''Display a single Person object.'''
    model = Person # retrieve Quote objects from the database
    template_name = "quotes/person.html" # delegate the display to this template
    context_object_name = "person" # use this variable name in the template


# Create your views here.
