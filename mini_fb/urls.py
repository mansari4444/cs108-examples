# mini_fb/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('create_profile', CreateProfileView.as_view(), name="create_profile"),

]