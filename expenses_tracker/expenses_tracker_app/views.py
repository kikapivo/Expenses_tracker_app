from django.shortcuts import render
from .models import Category
from .forms import CategoryForm

def index(request):
    """The home page for Expenses Tracker."""
    return render(request, 'expenses_tracker_app/index.html')


def categories(request):
    """Show all categories."""
    categories = Category.objects.order_by('date_added')
    context = {'categories':categories}
    return render(request,'expenses_tracker_app/categories.html',context)

def category(request, category_id):
    """Show a single category and all its entries."""
    category = Category.objects.get(id=category_id)
    entries = category.entry_set.order_by('-date_added')
    context={'category':category,'entries':entries}
    return render(request,'expenses_tracker_app/category.html',context)

def new_category(request):
    """Add a new category."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form=CategoryForm()
    else:
        # POST data submitted; process data.
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses_tracker_app:categories')
    #Display a blank or invalid form.
    context={'form': form}
    return render(request,'expenses_tracker_app/new_category.html',context)