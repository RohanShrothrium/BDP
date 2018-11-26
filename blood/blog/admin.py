from django.contrib import admin

# Register your models here.
from .models import Post
from . models import Enrolled
admin.site.register(Post)
admin.site.register(Enrolled)