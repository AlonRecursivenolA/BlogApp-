
from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views



urlpatterns = [
    path('register/',UserRegisterView.as_view(),name="register"),
    path('edit_profile/',UpdateFormView.as_view(),name='edit_profile'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='user_profile'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='user_profile_edit'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    # path('password-reset/', views.ChangePassword.as_view(), name='password-reset'),


]
