#forms.py

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to create a new profile object'''
    first_name = forms.CharField()
    last_name = forms.CharField()
    city = forms.CharField()
    email_address = forms.CharField()
    

    class Meta:
        '''Additional data about this form'''
        model = Profile # which model to create
        fields = ['first_name', 'last_name', 'city', 'email_address', 'image_url'] # which fields to create

class UpdateProfileForm(forms.ModelForm):
    '''A form to update profile object.'''

    class Meta:
        '''additional data about this form'''
        model = Profile # which model to create
        fields = ['city', 'email_address', 'image_url'] # which fields to create

class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create a new status message.'''
    
    class Meta:
        '''additional data about this form'''
        model = StatusMessage # which model to create
        fields = ['message', 'image'] # which fields to create
   