from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.

def index(request):
    """The home page for Blog"""
    return render(request,'blogs/index.html')

@login_required
def blog_posts(request):
    """Show all blog posts."""
    blog_posts = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'blog_posts':blog_posts}
    return render(request, 'blogs/blog_posts.html',context)

@login_required
def blog_post(request, blog_post_id):
    """Show a single blog post"""
    blog_post = BlogPost.objects.get(id = blog_post_id)
    #make sure the blog post belongs to the current user.
    if blog_post.owner !=request.user:
        raise Http404
    blog_content=blog_post.text
    context = {'blog_post':blog_post, 'blog_content':blog_content}
    return render(request, 'blogs/blog_post.html',context)

@login_required
def new_blog_post(request):
    """Add a new blog post."""
    if request.method !='POST':
        #no data submitted; create a blank form.
        form = BlogPostForm()
    else:
        #POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blog_post=form.save(commit=False)
            new_blog_post.owner=request.user
            new_blog_post.save()
            return redirect('blogs:blog_posts')

    #display a blank or invalid form. 
    context= {'form':form}
    return render(request, 'blogs/new_blog_post.html',context)

@login_required
def edit_blog_post(request):
    """Edit an existing blog post"""
    blog_posts = BlogPost.objects.all().filter(owner=request.user)
    for blog_post in blog_posts:
        if blog_post.owner !=request.user:
            raise Http404
        if request.method !='POST':
            #initial request; pre-fill form with the current entry
            form = BlogPostForm(instance = blog_post)
        else:
            #POST data submitted; process data.
            form = BlogPostForm(instance=blog_post, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('blogs:blog_post',blog_post_id= blog_post.id)
        context = {'blog_post':blog_post,'form':form}
        return render(request, 'blogs/edit_blog_post.html',context)

    