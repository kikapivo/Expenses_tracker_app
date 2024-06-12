"""Defines URL patterns for expenses_tracker_app."""
from django.urls import path
from . import views
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
]