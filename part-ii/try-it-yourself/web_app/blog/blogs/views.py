from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.

def index(request):
    """The home page for Blog"""
    return render(request,'blogs/index.html')

def blog_posts(request):
    """Show all blog posts."""
    if request.user.is_authenticated:
        blogposts1 = BlogPost.objects.filter(owner=request.user)
        blogposts2 = BlogPost.objects.filter(public=True)
        blog_posts = blogposts1.union(blogposts2).order_by('date_added')
    else: 
        blog_posts = BlogPost.objects.filter(public=True)
    context = {'blog_posts':blog_posts}
    return render(request, 'blogs/blog_posts.html',context)

def check_blog_post_public(request,blog_post_id):
    """check if the blogpost can be viewed by all users"""
    blog_post = BlogPost.objects.get(id=blog_post_id)
    if blog_post.public==False:
        check_blog_post_owner(request, blog_post_id)
    

def check_blog_post_owner(request,blog_post_id):
    """check if blog_post owner matches current user"""
    blog_post = BlogPost.objects.get(id=blog_post_id)
    if blog_post.owner != request.user:
        raise Http404 


def blog_post(request, blog_post_id):
    """Show a single blog post"""
    blog_post = get_object_or_404(BlogPost,id = blog_post_id)
    #make sure the blog post belongs to the current user.
    check_blog_post_public(request,blog_post_id)
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
            switch1 = request.POST.get('tog')
            if switch1 =="on":
                new_blog_post.public = True
            else:
                new_blog_post.public = False
            new_blog_post.save()
            return redirect('blogs:blog_posts')

    #display a blank or invalid form. 
    context= {'form':form}
    return render(request, 'blogs/new_blog_post.html',context)

@login_required
def edit_blog_post(request,blog_post_id):
    """Edit an existing blog post"""
    blog_post = BlogPost.objects.get(id=blog_post_id)
    if request.method !='POST':
        check_blog_post_owner(request,blog_post_id)
        #initial request; pre-fill form with the current entry
        form = BlogPostForm(instance = blog_post)
    else:
        check_blog_post_owner(request,blog_post_id)
        #POST data submitted; process data.
        form = BlogPostForm(instance=blog_post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_post',blog_post_id= blog_post.id)
    context = {'blog_post':blog_post,'form':form}
    return render(request, 'blogs/edit_blog_post.html',context)

    