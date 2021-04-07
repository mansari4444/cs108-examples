from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse
from .models import *
from .forms import *
from django import forms
import random

# Create your views here.

class ShowAllProfilesView(ListView):
    '''Show a facebook page'''
    model = Profile # retrieves Profile objects from the database
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"

class ShowProfilePageView(DetailView):
    '''Shows the profile of a single user'''
    model = Profile # retrieves Profile objects from the database
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "single_profile"

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
       
        return context

class CreateProfileView(CreateView):
    '''Create a new Profile object and store it in the database'''

    model = Profile # which model to create 
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView):
    '''Update a quote object and store it in the database.'''

    model = Profile # which model to create
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"

class DeleteStatusMessageView(DeleteView):
    '''Delete a quote object and store it in the database.'''

    model = Profile # which model to create
    template_name = "mini_fb/delete_status_form.html"
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['st_msg'] = st_msg
       
        return context
    
    def get_object(self):
        '''Return the StatusMessage object that should be deleted'''
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        status= StatusMessage.objects.filter(pk = status_pk, profile=profile_pk)
        
        return status
        # find the StatusMessage object, and return it

    def get_success_url(self):
            '''Return a the URL to which we should directed after the delete'''

            # get the pk for this quote
            profile_pk = self.kwargs['profile_pk']
            # pk = self.kwargs.get('pk')
            post_status = Profile.objects.filter(pk=profile_pk).first() # get one object from Queryset


            # find the person associated with the quote
            # show_profile_page = post_status.single_profile

            return reverse('show_profile_page', kwargs={'pk': post_status.pk})


def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile

            # now commit to database
            status_message.save()


    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)


class ShowNewsFeedView(DetailView):
    '''Shows NewsFeed for one profile.'''

    model = Profile
    template_name = "mini_fb/show_news_feed.html"
    context_object_name = "profile"

class ShowPossibleFriendsView(DetailView):
    '''Shows possible friends to add for a profile.'''

    model = Profile
    template_name = "mini_fb/show_possible_friends.html"
    context_object = "profile"

def add_friend(request, profile_pk, friend_pk):
    '''Processes the add friends request.'''

   
    first_profile = Profile.objects.get(pk=profile_pk)

    second_profile = Profile.objects.get(pk=friend_pk)

    first_profile.friends.add(second_profile)

    first_profile.save()

    url = reverse('show_profile_page', kwargs={'pk': profile_pk})

    return redirect(url)


    





