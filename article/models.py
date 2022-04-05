
from pyexpat import model
from unicodedata import category
from django.db import models
from django.forms import ChoiceField, DateTimeField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from matplotlib.image import thumbnail
User = get_user_model()
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length = 255, name = "category")
    def __str__(self):
        return self.category
    
class HashTag(models.Model):
    tagname1 = models.CharField(max_length = 255, name = "tagname1")
    def __str__(self):
        return self.tagname1

class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="author2")
    title = models.CharField(max_length = 255, name= "title")
    date = models.DateTimeField(auto_now_add = True)
    thumbnail = models.ImageField( upload_to="articles/thumbnail/")
    content = RichTextUploadingField()
    # image2 = models.ImageField( upload_to="articles/thumbnail/",  null=True, blank= True)
    # content_part2 = RichTextField(null = True, blank= True)
    # image3 = models.ImageField( upload_to="articles/thumbnail/", null=True, blank= True)
    # content_part3 = RichTextField(null = True, blank= True)
    # image4 = models.ImageField( upload_to="articles/thumbnail/" , null=True, blank= True)
    # content_part4 = RichTextField(null = True, blank= True)
    # image5 = models.ImageField( upload_to="articles/thumbnail/" ,  null=True, blank= True)
    # content_part5 = RichTextField( null = True, blank= True)
    # image6 = models.ImageField( upload_to="articles/thumbnail/" , null=True, blank= True)
    # content_part6 = RichTextField(null = True, blank= True)
    category =models.ForeignKey(Category, on_delete=models.PROTECT)
    hashtag  =models.ForeignKey(HashTag, on_delete=models.CASCADE, null= True, blank=True )
    
    def __str__(self):
            return self.title
    class Meta:
        ordering = ['-id']

