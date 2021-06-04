from django.contrib import admin
from blog.models import Post,Comment # < here

admin.site.register(Post) # < here
admin.site.register(Comment)