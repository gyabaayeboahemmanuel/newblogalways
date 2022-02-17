from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from .models import *

def blog_post (request):
    blog = Blog.objects.all()
    context = {
        "blog":blog,

    }
    return render(request, "blog/blogs.html", context)
