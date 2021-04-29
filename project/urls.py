# project/urls.py

from django.urls import path
from .views import * # imports all the views 

urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"), # the default link that takes you to the homepage 
    path('boat/<int:pk>', Specific_boat_PageView.as_view(), name="boat"), # uses pk to specify which boat 
    path('guide/<int:pk>', GuidePageView.as_view(), name="guide"), # uses pk to specify which guide 
    path('create_booking', CreateBookingView.as_view(), name="create_booking"), # a link to create a new booking object 
    path('booking/<int:pk>', BookingPageView.as_view(), name="booking"), # uses pk to specify which booking 
    path('all_bookings', AllBookingPageView.as_view(), name="all_bookings"), # a link to all bookings
    path('booking/<int:pk>/update', UpdateBookingView.as_view(), name="update_booking"), # a link to update booking uses the pk of the booking 
    path('new_customer', NewCustomerView.as_view(), name="new_customer"), # a link to create a new customer
    path('booking/<int:pk>/delete', DeleteBookingView.as_view(), name="delete_booking"), # a link to delete a booking uses the pk of the booking
    path('customer/<int:pk>', CustomerView.as_view(), name="customer"), # uses pk to specify which customer 
    path('all_customers', AllCustomersView.as_view(), name="all_customers"), # a link to see all customers view
    path('all_guides', AllGuidesView.as_view(), name="all_guides"), # a link to show all guides view
    path('customer/<int:pk>/delete', DeleteCustomerView.as_view(), name="delete_customer"), # a link to delete a customer using the customers pk
    path('new_guide', NewGuideView.as_view(), name="new_guide"), # a link to add a new guide
    path('guide/<int:pk>/delete', DeleteGuideView.as_view(), name="delete_guide"), # a link to delete a guide using the guides pk
    path('new_boat', NewBoatView.as_view(), name="new_boat"), # link to new boat view
    path('boat/<int:pk>/delete', DeleteBoatView.as_view(), name="delete_boat"), # a link to delete a boat object using the boats pk
    path('guide/<int:pk>/update', UpdateGuideView.as_view(), name="update_guide"), # a link to update the guides profile using the guides pk
    path('boat/<int:pk>/update', UpdateBoatView.as_view(), name="update_boat"), # a link to update the boat and locations profile using the boats pk












    

    
    


]