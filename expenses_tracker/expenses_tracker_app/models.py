from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific about a category of the expense."""
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name_plural="entries"
    def __str__(self):
        return f"{self.text[:50]}..."


class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.category} - ${self.amount}"