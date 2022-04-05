import imp
from unicodedata import name
from django.urls import path, re_path
from .views import *
app_name = "account"
urlpatterns = [   
    path ("blogs/", all_blogs_view, name = "blogs_view"),
    path("<int:id>/", single_blog_view , name="view_single_blog"),   
]