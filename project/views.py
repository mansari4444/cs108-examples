from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse
from .models import *
# from .forms import *
# from django import forms
import random
# Create your views here.

class HomePageView(ListView):
    '''Show a list of boats available and locations they service.'''
    model = Boat # retrieve Boat objects from the databse
    template_name = "project/home.html"
    context_object_name = "boats"