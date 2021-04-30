"""TechStartBackEnd URL Configurations

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from BackEnd import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('news-section', views.getNewsSection.as_view(), name='News Sections'),
    path('news-section/create', views.saveNewsSection.as_view(), name='Save News Section'),
    path('news-section/<int:pk>', views.updateNewsSection.as_view(), name='Update News Section'),
    path('news-section/<int:pk>/delete', views.deleteNewsSection.as_view(), name='Delete News Section'),
    path('news', views.getNews.as_view(), name='News'),
    path('news/create', views.saveNews.as_view(), name='Save News'),
    path('news/<int:pk>', views.updateNews.as_view(), name='Update News'),
    path('news/<int:pk>/delete', views.deleteNews.as_view(), name='Delete News'),
    path('post', views.getPost.as_view(), name='Posts'),
    path('post/create', views.savePost.as_view(), name='Save Post'),
    path('post/<int:pk>', views.updatePost.as_view(), name='Update Post'),
    path('update-post/<int:pk>', views.updateUserPost.as_view(), name='Update User Post'),
    path('post/<int:pk>/delete', views.deletePost.as_view(), name='Delete Post'),
    path('comment', views.getComment.as_view(), name='Comments'),
    path('comment/create', views.saveComment.as_view(), name='Save Comment'),
    path('comment/<int:pk>', views.updateComment.as_view(), name='Update Comment'),
    path('comment/<int:pk>/delete', views.deleteComment.as_view(), name='Delete Comment'),
    path('login', obtain_auth_token, name='API Token Login'),
    path('register', views.RegisterUserView.as_view(), name='Register user')
]
