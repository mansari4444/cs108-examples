from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quote, Person
from django.urls import reverse
from .forms import CreateQuoteForm, UpdateQuoteForm, AddImageForm
from django.shortcuts import redirect
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
    #context_object_name = "person" # use this variable name in the template

    def get_context_data(self, **kwargs):

        # get the default context data:
        # this will include the person record for this page view
        context = super(PersonPageView, self).get_context_data(**kwargs)

        # create add image form:
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form

        # return the context dictionary
        return context
class CreateQuoteView(CreateView):
    '''Create a new quote object and store it in the database.'''

    model = Quote # which model to create
    form_class = CreateQuoteForm
    template_name = "quotes/create_quote_form.html"

class UpdateQuoteView(UpdateView):
    '''Update a quote object and store it in the database.'''

    model = Quote # which model to create
    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote_form.html"

class DeleteQuoteView(DeleteView):
    '''Update a quote object and store it in the database.'''

    model = Quote # which model to create
    template_name = "quotes/delete_quote_form.html"
    queryset = Quote.objects.all()
    # success_url = "../../all" # what to do after deleting a quote

    def get_success_url(self):
        '''Return a the URL to which we should directed after the delete'''

        # get the pk for this quote
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first() # get one object from Queryset

        # find the person associated with the quote
        person = quote.person
        return reverse('person', kwargs={'pk':person.pk})


def add_image(request, pk):
    '''A custom view function to handle the submission of an image uploud'''

    # find the person for whom we are submitting the image
    person = Person.objects.get(pk=pk)

    # read the request data into AddImageForm object
    form = AddImageForm(request.POST or None, request.FILES or None)

    # check if the form is valid, save object to database
    if form.is_valid():

        image = form.save(commit=False) # create the Image object but not save it
        image.person = person
        image.save() # store to the database
    else:
        print("Error: the form was not valid")

    # redirect to a new URL, display person page

    url = reverse('person', kwargs={'pk':pk})
    return redirect(url)


# Create your views here.
