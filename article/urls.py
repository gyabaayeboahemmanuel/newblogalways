from unicodedata import name
from django.urls import path, re_path
from .views import *
app_name = "article"
urlpatterns = [
    path("", article, name="article" ),
    path("post/add", post_article, name="post_article"),
    #path("post/edit", edit_article, name="edit_article_post"),
    path("<int:id>/article_detail", article_details, name="article_details"), 
    path("tag/<str:tagname>/", tag_name, name="tag_name" ),  
]
