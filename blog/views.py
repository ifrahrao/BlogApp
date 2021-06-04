from django.shortcuts import render,redirect, reverse

from blog.models import Post # < here
from .forms import  CommentForm

def index(request, slug=None): # < here
    posts = Post.objects.all()
    return render(request,
                  'blog/index.html',
                  {
                      'posts': posts,
                      'section': 'blog_index'
                  })


def detail(request, slug=None): # < here
    post = Post.objects.get(slug=slug)
    comment_form = CommentForm()
    if request.method == 'POST':
      comment_form = CommentForm(data=request.POST)
      if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        # Assign the current post to the comment
        new_comment.post = post
        # Save the comment to the database
        new_comment.save()
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm()
        return render(request,
                  'blog/detail.html',
                  {
                      'post': post,
                      'comment_form': comment_form,
                      'section': 'blog_detail'
                  })
    else:
      comment_form = CommentForm()
    return render(request,
                  'blog/detail.html',
                  {
                      'post': post,
                      'comment_form': comment_form,
                      'section': 'blog_detail'
                  })


def home(request): # < here
    return render(request,
                  'home.html',
                  {'section': 'home'})