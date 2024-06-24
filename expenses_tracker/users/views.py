from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a new user."""
    if request.method !='POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('expenses_tracker_app:index')

    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def about(request):
    return render(request, 'expenses_tracker_app/about.html', {'title': 'About'})

def privacy_policy(request):
    return render(request, 'privacy_policy.html')
# Create your views here.
