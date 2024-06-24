"""Defines URL patterns for expenses_tracker_app."""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView


app_name="expenses_tracker_app"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all categories
    path('categories/', views.categories, name='categories'),
    #Detail page for a single category
    path('categories/<int:category_id>/', views.category, name='category'),
    #Page for adding a new category
    path('new_category/',views.new_category,name='new_category'),
    #Page for editing an entry
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
    # Page for adding a new entry
    path('new_entry/<int:category_id>/', views.new_entry, name='new_entry'),
    path('expenses/', views.expenses_list, name='expenses_list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', views.about, name='expenses_tracker_app-about'),
    path('footer/', views.footer, name='footer'),
    path('privacy/', TemplateView.as_view(template_name='expenses_tracker_app/privacy_policy.html'), name='privacy_policy'),
]