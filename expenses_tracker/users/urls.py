"""Defines URL patterns for users"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views


from . import views

app_name='users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    #Registration page.
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('about/', views.about, name='expenses_tracker_app-about'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]