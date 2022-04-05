import django
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register (Articles)
admin.site.register(Category)
admin.site.register(HashTag)
admin.site.site_header = "Blog Always Admin"
admin.site.site_title = "Blog Always Admin Portal"
admin.site.index_title = "Welcome to Blog Always Admin Portal"