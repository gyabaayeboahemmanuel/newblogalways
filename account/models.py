from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Profile2 (models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name="profile2")
    firstName = models.CharField(max_length= 255)
    lastName = models.CharField(max_length= 255)
    profile_picture = models.ImageField(upload_to = "profile/")
    dateSignedUp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-user",)
    def __str__(self) -> str:
        return self.firstName + " "+ self.lastName
