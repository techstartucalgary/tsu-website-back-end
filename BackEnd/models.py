from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class EventSection(models.Model):
    event_category = models.CharField(max_length=200)
    def __str__(self):
        return str(self.event_category)

class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(EventSection, on_delete=models.CASCADE)
    event_description = models.CharField(max_length=10000000)
    date_published = models.DateField()
    # image = models.ImageField()
    source = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    # tags = models.CharField(max_length=200) 
    def __str__(self):
        return str(self.title)

class Post(models.Model): 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_posted = models.DateField()
    post_description = models.TextField(max_length=10000000)
    # tags = models.CharField(max_length=200)
    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_description = models.TextField(max_length=10000000)
    date_commented = models.DateField()

    def __str__(self):
        return str(self.comment_description)
