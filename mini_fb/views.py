from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

# Create your views here.

class ShowAllProfilesView(ListView):
    '''Show a facebook page'''
    model = Profile # retrieves Profile objects form the database
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "mini_fbs"

