"""Defines URL patterns for learning_logs"""

from django.urls import path

from .import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('',views.index,name='index'),
    #page that shows all topics.
    path('topics/',views.topics, name ='topics'),
    #detail page for a single topic.
    path('topics/<int:topic_id>/',views.topic, name='topic'),
]