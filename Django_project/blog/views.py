from django.shortcuts import render
from .models import Post
def index(request):
    posts =	Post.objects.all()
    return render(
        request,	
        'blog/index.html',
        {
            'posts': posts
        }
    )
def single_post_page(request,	value):
    post =	Post.objects.get(pk=value)
    return render(
        request,	
        'blog/single_post_page.html',
        {
            'post' :	post,
        }
    )

def aa_page(request):
    return render(
        request,
        'blog/aa.html',
    )