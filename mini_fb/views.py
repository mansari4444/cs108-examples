from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile
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



    


