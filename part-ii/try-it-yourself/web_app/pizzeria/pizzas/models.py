from django.db import models

# Create your models here.

class Pizza(models.Model):
    """Define kinds of pizzas"""
    name=models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Topping(models.Model):
    """Toppings that are added to the different kinds of pizza"""
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.name) >50:
            return f"{self.name[:50]}..."
        else: 
            return f"{self.name}"