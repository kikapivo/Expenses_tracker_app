from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Category, Entry, Expenses
from .forms import CategoryForm, EntryForm
from  django.http import Http404

def index(request):
    """The home page for Expenses Tracker."""
    return render(request, 'expenses_tracker_app/index.html')


@login_required
def expenses_list(request):
    expenses = Expenses.objects.all()
    return render(request, 'expenses_list.html', {'expenses: expenses'})

@login_required
def categories(request):
    """Show all categories."""
    categories = Category.objects.filter(owner=request.user).order_by('date_added')
    context = {'categories':categories}
    return render(request,'expenses_tracker_app/categories.html',context)

@login_required
def category(request, category_id):
    """Show a single category and all its entries."""
    category = Category.objects.get(id=category_id)
    # Make sure the topic belongs to the current user.
    if category.owner != request.user:
        raise Http404
    entries = category.entry_set.order_by('-date_added')
    context={'category':category,'entries':entries}
    return render(request,'expenses_tracker_app/category.html',context)

@login_required
def new_category(request):
    """Add a new category."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form=CategoryForm()
    else:
        # POST data submitted; process data.
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.owner = request.user
            new_category.save()
            form.save()
            return redirect('expenses_tracker_app:categories')
    #Display a blank or invalid form.
    context={'form': form}
    return render(request,'expenses_tracker_app/new_category.html',context)

@login_required
def new_entry(request, category_id):
    """"Add a new entry for a particular category."""
    category = Category.objects.get(id=category_id)

    if request.method == 'POST':
        #POST data submitted; process data.
        form = EntryForm (data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.category = category
            new_entry.save()
            return redirect('expenses_tracker_app:category', category_id=category_id)
    else:
        # No data submitted; create a blank form.
        form=EntryForm()

    #Display a blank or invalid form.
    context={'category': category, 'form': form}
    return render(request, 'expenses_tracker_app/new_entry.html',context)


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    category = entry.category
    if category.owner != request.user:
        raise Http404

    if request.method!= 'POST':
        #Initial request; pre-fill form with the current entry.
        form=EntryForm(instance=entry)
    else:
        #POST data submitted;process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses_tracker_app:category',category_id=category.id)

    context= {'entry': entry, 'category': category, 'form': form}
    return render(request,'expenses_tracker_app/edit_entry.html',context)

def about(request):
    return render(request, 'expenses_tracker_app/about.html', {'title': 'About'})

def footer(request):
    return HttpResponse(request,'footer.html')
