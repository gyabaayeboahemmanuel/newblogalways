from django.db import models
from django.forms import DateTimeField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 255, name= "title")
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title

class images (models.Model):
    post = models.ForeignKey("Blog", on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "media/images")
    
class text (models.Model):
    post = models.ForeignKey("Blog", on_delete=models.CASCADE)
    text = models.TextField()
