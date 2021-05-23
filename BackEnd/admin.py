from django.contrib import admin
from .models import EventSection, Event, Post, Comment

# Register your models here.

admin.site.register(EventSection)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Comment)