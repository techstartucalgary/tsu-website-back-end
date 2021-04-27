from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class NewsSection(models.Model):
    news_category = models.CharField(max_length=200)
    def __str__(self):
        return str(self.news_category)

class News(models.Model):

    
    title = models.CharField(max_length=200)
    category = models.ForeignKey(NewsSection, on_delete=models.CASCADE)
    news_description = models.CharField(max_length=10000000)
    date_published = models.DateField()
    # image = models.ImageField()
    source = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    # tags = models.CharField(max_length=200) 
    def __str__(self):
        return str(self.title)

# automatic account system

# class Account(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)    # special field
#     password = models.CharField(max_length=200) # special field
#     # profile_picture = models.ImageField()
#     degree = models.CharField(max_length=200)

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
