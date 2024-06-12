from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField


class Category(models.Model):
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.text

class Entry(models.Model):
    """Something specific learned about a category."""
    topic=models.ForeignKey(Category,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="entries"
        def __str__(self):
            return f"{self.text[:50]}..."
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date= models.DateField(auto_now_add=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.category}: {self.amount} on {self.date}"

