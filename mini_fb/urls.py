# mini_fb/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('profile/<int:pk>/post_status', post_status_message, name="post_status_message"),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name="delete_post_status_message"),
    path('create_profile', CreateProfileView.as_view(), name="create_profile"),
    path('profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name="show_news_feed"),
    path('profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name="show_possible_friends"),
    path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', add_friend, name="add_friend"),

]