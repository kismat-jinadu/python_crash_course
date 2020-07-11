"""Defines URL patterns for pizzas"""

from django.urls import path

from .import views

app_name = 'pizzas'
urlpatterns = [
    #Home page
    path('',views.index,name='index'),
    #page that shows all pizza names
    path('pizza_names/',views.pizza_names, name ='pizza_names'),
    #detail page for a single pizza_name.
    path('pizza_names/<int:pizza_name_id>/',views.pizza_name, name='pizza_name'),
]