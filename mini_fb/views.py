from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Profile
from .forms import CreateProfileForm, UpdateProfileForm
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




    


