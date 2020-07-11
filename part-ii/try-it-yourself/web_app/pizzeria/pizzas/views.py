from django.shortcuts import render

from .models import Pizza
# Create your views here.

def index(request):
    """The home page for Pizzas."""
    return render(request, 'pizzas/index.html')

def pizza_names(request):
    """Show all pizza_names."""
    pizza_names = Pizza.objects.order_by('date_added')
    context={'pizza_names':pizza_names}
    return render(request, 'pizzas/pizza_names.html',context)

def pizza_name(request, pizza_name_id):
    """Show a single pizza_name and all its toppings."""
    pizza_name = Pizza.objects.get(id=pizza_name_id)
    toppings = pizza_name.topping_set.order_by('-date_added')
    context ={'pizza_name':pizza_name, 'toppings':toppings}
    return render(request,'pizzas/pizza_name.html',context)

