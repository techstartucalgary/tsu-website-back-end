from django.contrib import admin
from .models import NewsSection, News, Post, Comment

# Register your models here.


admin.site.register(NewsSection)
admin.site.register(News)
admin.site.register(Post)
admin.site.register(Comment)