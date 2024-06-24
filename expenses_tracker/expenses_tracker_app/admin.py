from django.contrib import admin
from .models import Category, Entry, Expenses
admin.site.register(Category)
admin.site.register(Entry)
admin.site.register(Expenses)