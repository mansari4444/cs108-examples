# project/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    path('boat/<int:pk>', Specific_boat_PageView.as_view(), name="boat"),
    path('guide/<int:pk>', GuidePageView.as_view(), name="guide"),
    path('create_booking', CreateBookingView.as_view(), name="create_booking"),
    path('booking/<int:pk>', BookingPageView.as_view(), name="booking"),
    path('all_bookings', AllBookingPageView.as_view(), name="all_bookings"),
    path('booking/<int:pk>/update', UpdateBookingView.as_view(), name="update_booking"),
    path('new_customer', NewCustomerView.as_view(), name="new_customer"),
    path('booking/<int:pk>/delete', DeleteBookingView.as_view(), name="delete_booking"),
    path('customer/<int:pk>', CustomerView.as_view(), name="customer"),
    path('all_customers', AllCustomersView.as_view(), name="all_customers"),
    path('all_guides', AllGuidesView.as_view(), name="all_guides"),
    path('customer/<int:pk>/delete', DeleteCustomerView.as_view(), name="delete_customer"),
    path('new_guide', NewGuideView.as_view(), name="new_guide"),
    path('guide/<int:pk>/delete', DeleteGuideView.as_view(), name="delete_guide"),
    path('new_boat', NewBoatView.as_view(), name="new_boat"),
    path('boat/<int:pk>/delete', DeleteBoatView.as_view(), name="delete_boat"),










    

    
    


]