"""Defines URL patterns for blogs."""

from django.urls import path

from .import views

app_name ='blogs'

urlpatterns =[
  #Home page
  path('',views.index, name='index'),
  #Page that shows all blog posts
  path('blogposts/',views.blog_posts,name = 'blog_posts'),
  #page that displays a single blog post
  path('blogposts/<int:blog_post_id>/',views.blog_post,name = 'blog_post'),
  #page for adding a new blog post
  path('newblogpost/', views.new_blog_post,name='new_blog_post'),
  #page for editing single blog post
  path('blogpost/editblogpost/',views.edit_blog_post,name = 'edit_blog_post'),
]