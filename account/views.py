from django.core.checks import messages
from django.shortcuts import redirect, render, get_object_or_404
from matplotlib.style import context
from .forms import *
from django.contrib import messages
import random
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
User = get_user_model()
# Create your views here.

def signup(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST, files=request.FILES)
        profile_form = UserProfileForm(data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            profile.user = user
            user.save()
            profile.save()
            messages.success(request, 'user created')
            return redirect("/")
        else:
            messages.warning(request, "invalid data entry")

    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'registration/signup.html', 
        {
        "user_form": user_form,
        "profile_form" : profile_form
        })


def login (request): 
    if request.method == "POST":
        user_login = LoginForm(data=request.POST, files=request.FILES)
        if user_login.is_valid():
            print("user details saved")
    else: 
        user_login = LoginForm()
  

        
    return render(request, "registration/login.html", {
        "loginform": user_login
        })

# @login_required
# def edit_user_profile(request, pk):
#     userform = get_object_or_404(User, pk=pk)
#     userprofileform = get_object_or_404(Profile, pk=pk)
#     if request.method == "POST":
#         print("..................geting reqeust ....................")
#         user_form = UserForm(data=request.POST, files=request.FILES, instance = userform)
#         profile_form = UserProfileForm(data=request.POST, files=request.FILES, instance = userprofileform)
#         print("..................form recived....................")
        
#         if user_form.is_valid() and profile_form.is_valid():
#             print("..................data to be saved....................")
           
#             user = user_form.save(commit=False)
#             profile = profile_form.save(commit=False)
#             user.username = user.first_name + str(random.randint(0, 1000))
#             user.password = "something.random_here"
#             user.password2 = "something.random_here"
#             user.save()
#             profile.user = user
#             profile.save()

#             messages.success(request, 'user created')
#             return redirect("")
#         else:
#             print("..................data not saved ....................")

#             messages.warning(request, "invalid data entry")

#     else:
#         print(".................form not gotten ....................")

#         user_form = UserForm(instance = userform)
#         profile_form = UserProfileForm(isntance = userprofileform)

#     return render(request, 'registration/signup.html', 
#         {
#         "user_form": user_form,
#         "profile_form" : profile_form
#         })
           
    

def all_blogs_view(request):
    users = User.objects.all()

    return render(request, "blog/blog.html",
    {
        "users": users,
        
    })
def single_blog_view(request, id):
    user = get_object_or_404(User, id = id)

    return render(request, "blog/single_blog_page.html",
    {
        "user": user,
     
    })